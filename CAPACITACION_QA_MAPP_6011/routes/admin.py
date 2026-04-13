"""Admin routes for progress tracking and calendar."""
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db
from data.training_content import WEEKS, get_all_modules, get_module_by_id

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/admin/progreso", response_class=HTMLResponse)
async def panel_progreso(request: Request):
    """Admin view: team progress overview."""
    db = await get_db()
    colaboradores = await db.execute_fetchall(
        "SELECT * FROM colaboradores WHERE activo=1 ORDER BY nombre"
    )
    all_modules = get_all_modules()
    total_modulos = len(all_modules)

    team_progress = []
    for col in colaboradores:
        progreso = await db.execute_fetchall(
            "SELECT modulo_id, completado FROM progreso_modulos WHERE colaborador_id=?",
            (col[0],),
        )
        completados = sum(1 for p in progreso if p[1] == 1)

        tests = await db.execute_fetchall(
            "SELECT modulo_id, MAX(porcentaje) as mejor, aprobado FROM resultados_test WHERE colaborador_id=? GROUP BY modulo_id",
            (col[0],),
        )
        aprobados = sum(1 for t in tests if t[2] == 1)
        promedio_notas = round(sum(t[1] for t in tests) / len(tests)) if tests else 0

        team_progress.append({
            "colaborador": col,
            "completados": completados,
            "total": total_modulos,
            "porcentaje": round((completados / total_modulos) * 100) if total_modulos else 0,
            "tests_aprobados": aprobados,
            "promedio_notas": promedio_notas,
        })

    await db.close()
    return templates.TemplateResponse("admin_progress.html", {
        "request": request,
        "team_progress": team_progress,
        "weeks": WEEKS,
        "total_modulos": total_modulos,
    })


@router.get("/admin/progreso/{colaborador_id}", response_class=HTMLResponse)
async def detalle_colaborador(request: Request, colaborador_id: int):
    """Detailed progress view for a single colaborador."""
    db = await get_db()
    rows = await db.execute_fetchall(
        "SELECT * FROM colaboradores WHERE id=?", (colaborador_id,)
    )
    if not rows:
        await db.close()
        return RedirectResponse(url="/admin/progreso")
    colaborador = rows[0]

    all_modules = get_all_modules()
    total_modulos = len(all_modules)

    # Progress per module
    progreso_rows = await db.execute_fetchall(
        "SELECT modulo_id, completado, fecha_inicio, fecha_completado "
        "FROM progreso_modulos WHERE colaborador_id=?",
        (colaborador_id,),
    )
    progreso_dict = {
        r[0]: {"completado": r[1], "fecha_inicio": r[2], "fecha_completado": r[3]}
        for r in progreso_rows
    }
    completados = sum(1 for v in progreso_dict.values() if v["completado"] == 1)
    porcentaje_global = round((completados / total_modulos) * 100) if total_modulos else 0

    # All test attempts (history)
    historial_tests = await db.execute_fetchall(
        "SELECT modulo_id, puntaje, total_preguntas, porcentaje, aprobado, fecha "
        "FROM resultados_test WHERE colaborador_id=? ORDER BY fecha DESC",
        (colaborador_id,),
    )

    # Best score per module
    mejores_tests = await db.execute_fetchall(
        "SELECT modulo_id, MAX(porcentaje) as mejor, aprobado "
        "FROM resultados_test WHERE colaborador_id=? GROUP BY modulo_id",
        (colaborador_id,),
    )
    mejores_dict = {r[0]: {"mejor": r[1], "aprobado": r[2]} for r in mejores_tests}
    tests_aprobados = sum(1 for v in mejores_dict.values() if v["aprobado"] == 1)
    promedio = (
        round(sum(v["mejor"] for v in mejores_dict.values()) / len(mejores_dict))
        if mejores_dict else 0
    )

    # Build week-by-week detail
    weeks_detail = []
    for week in WEEKS:
        mods_detail = []
        for mod in week["modulos"]:
            mid = mod["id"]
            prog = progreso_dict.get(mid, {})
            test = mejores_dict.get(mid, {})
            mods_detail.append({
                "id": mid,
                "nombre": mod["nombre"],
                "procedimiento": mod["procedimiento"],
                "completado": prog.get("completado", 0),
                "fecha_inicio": prog.get("fecha_inicio"),
                "fecha_completado": prog.get("fecha_completado"),
                "mejor_nota": test.get("mejor"),
                "aprobado": test.get("aprobado", 0),
                "num_preguntas": len(mod["preguntas"]),
            })
        week_completados = sum(1 for m in mods_detail if m["completado"] == 1)
        weeks_detail.append({
            "semana": week["semana"],
            "titulo": week["titulo"],
            "descripcion": week["descripcion"],
            "modulos": mods_detail,
            "completados": week_completados,
            "total": len(mods_detail),
            "porcentaje": round((week_completados / len(mods_detail)) * 100) if mods_detail else 0,
        })

    # Enrich test history with module names
    historial_enriched = []
    for t in historial_tests:
        mod = get_module_by_id(t[0])
        historial_enriched.append({
            "modulo_id": t[0],
            "modulo_nombre": mod["nombre"] if mod else t[0],
            "puntaje": t[1],
            "total_preguntas": t[2],
            "porcentaje": t[3],
            "aprobado": t[4],
            "fecha": t[5],
        })

    await db.close()
    return templates.TemplateResponse("admin_detail.html", {
        "request": request,
        "colaborador": colaborador,
        "weeks_detail": weeks_detail,
        "historial_tests": historial_enriched,
        "porcentaje_global": porcentaje_global,
        "completados": completados,
        "total_modulos": total_modulos,
        "tests_aprobados": tests_aprobados,
        "promedio": promedio,
        "total_intentos": len(historial_tests),
    })


@router.get("/admin/calendario", response_class=HTMLResponse)
async def ver_calendario(request: Request):
    """Admin view: training calendar."""
    db = await get_db()
    sesiones = await db.execute_fetchall(
        "SELECT * FROM sesiones_calendario ORDER BY semana, fecha_programada"
    )
    await db.close()
    return templates.TemplateResponse("calendar.html", {
        "request": request,
        "weeks": WEEKS,
        "sesiones": sesiones,
    })


@router.post("/admin/calendario/agregar")
async def agregar_sesion(
    request: Request,
    semana: int = Form(...),
    fecha_programada: str = Form(...),
    duracion_min: int = Form(60),
    notas: str = Form(""),
):
    """Add a training session to the calendar."""
    week_data = None
    for w in WEEKS:
        if w["semana"] == semana:
            week_data = w
            break

    if not week_data:
        return RedirectResponse(url="/admin/calendario", status_code=303)

    db = await get_db()
    await db.execute(
        "INSERT INTO sesiones_calendario (semana, titulo, descripcion, fecha_programada, duracion_min, notas) VALUES (?, ?, ?, ?, ?, ?)",
        (semana, week_data["titulo"], week_data["descripcion"], fecha_programada, duracion_min, notas),
    )
    await db.commit()
    await db.close()
    return RedirectResponse(url="/admin/calendario", status_code=303)


@router.post("/admin/calendario/estado/{sesion_id}")
async def cambiar_estado(request: Request, sesion_id: int, estado: str = Form(...)):
    """Update session status."""
    db = await get_db()
    await db.execute(
        "UPDATE sesiones_calendario SET estado=? WHERE id=?",
        (estado, sesion_id),
    )
    await db.commit()
    await db.close()
    return RedirectResponse(url="/admin/calendario", status_code=303)
