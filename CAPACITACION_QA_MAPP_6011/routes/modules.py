"""Module and learning routes."""
import json
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db
from data.training_content import WEEKS, get_module_by_id, get_all_modules

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/dashboard/{colaborador_id}", response_class=HTMLResponse)
async def dashboard(request: Request, colaborador_id: int):
    """Main dashboard with weekly overview and progress."""
    db = await get_db()
    colaborador = await db.execute_fetchall(
        "SELECT * FROM colaboradores WHERE id=?", (colaborador_id,)
    )
    if not colaborador:
        await db.close()
        return RedirectResponse(url="/")
    colaborador = colaborador[0]

    # Get progress for all modules
    progreso = await db.execute_fetchall(
        "SELECT modulo_id, completado FROM progreso_modulos WHERE colaborador_id=?",
        (colaborador_id,),
    )
    progreso_dict = {row[0]: row[1] for row in progreso}

    # Get test results
    tests = await db.execute_fetchall(
        "SELECT modulo_id, MAX(porcentaje) as mejor_nota, aprobado FROM resultados_test WHERE colaborador_id=? GROUP BY modulo_id",
        (colaborador_id,),
    )
    tests_dict = {row[0]: {"nota": row[1], "aprobado": row[2]} for row in tests}

    # Calculate overall progress
    all_modules = get_all_modules()
    total = len(all_modules)
    completados = sum(1 for m in all_modules if progreso_dict.get(m["id"], 0) == 1)
    porcentaje_global = round((completados / total) * 100) if total > 0 else 0

    await db.close()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "colaborador": colaborador,
        "weeks": WEEKS,
        "progreso": progreso_dict,
        "tests": tests_dict,
        "porcentaje_global": porcentaje_global,
        "completados": completados,
        "total": total,
    })


@router.get("/modulo/{colaborador_id}/{modulo_id}", response_class=HTMLResponse)
async def ver_modulo(request: Request, colaborador_id: int, modulo_id: str):
    """View a specific training module."""
    modulo = get_module_by_id(modulo_id)
    if not modulo:
        return RedirectResponse(url=f"/dashboard/{colaborador_id}")

    db = await get_db()
    colaborador = await db.execute_fetchall(
        "SELECT * FROM colaboradores WHERE id=?", (colaborador_id,)
    )
    colaborador = colaborador[0] if colaborador else None

    # Mark module as started
    await db.execute(
        "INSERT OR IGNORE INTO progreso_modulos (colaborador_id, modulo_id, fecha_inicio) VALUES (?, ?, datetime('now'))",
        (colaborador_id, modulo_id),
    )
    await db.commit()

    # Check if already completed
    progreso = await db.execute_fetchall(
        "SELECT completado FROM progreso_modulos WHERE colaborador_id=? AND modulo_id=?",
        (colaborador_id, modulo_id),
    )
    completado = progreso[0][0] if progreso else 0

    # Get best test score
    test_result = await db.execute_fetchall(
        "SELECT MAX(porcentaje) as mejor, aprobado FROM resultados_test WHERE colaborador_id=? AND modulo_id=?",
        (colaborador_id, modulo_id),
    )
    mejor_nota = test_result[0][0] if test_result and test_result[0][0] else None

    await db.close()
    return templates.TemplateResponse("module.html", {
        "request": request,
        "colaborador": colaborador,
        "modulo": modulo,
        "completado": completado,
        "mejor_nota": mejor_nota,
    })


@router.post("/completar/{colaborador_id}/{modulo_id}")
async def completar_modulo(request: Request, colaborador_id: int, modulo_id: str):
    """Mark a module as completed."""
    db = await get_db()
    await db.execute(
        "UPDATE progreso_modulos SET completado=1, fecha_completado=datetime('now') WHERE colaborador_id=? AND modulo_id=?",
        (colaborador_id, modulo_id),
    )
    await db.commit()
    await db.close()
    return RedirectResponse(url=f"/modulo/{colaborador_id}/{modulo_id}", status_code=303)


@router.get("/test/{colaborador_id}/{modulo_id}", response_class=HTMLResponse)
async def ver_test(request: Request, colaborador_id: int, modulo_id: str):
    """Show the test for a module."""
    modulo = get_module_by_id(modulo_id)
    if not modulo:
        return RedirectResponse(url=f"/dashboard/{colaborador_id}")

    db = await get_db()
    colaborador = await db.execute_fetchall(
        "SELECT * FROM colaboradores WHERE id=?", (colaborador_id,)
    )
    colaborador = colaborador[0] if colaborador else None
    await db.close()

    return templates.TemplateResponse("test.html", {
        "request": request,
        "colaborador": colaborador,
        "modulo": modulo,
    })


@router.post("/test/{colaborador_id}/{modulo_id}")
async def enviar_test(request: Request, colaborador_id: int, modulo_id: str):
    """Process test submission."""
    modulo = get_module_by_id(modulo_id)
    if not modulo:
        return RedirectResponse(url=f"/dashboard/{colaborador_id}")

    form_data = await request.form()
    preguntas = modulo["preguntas"]
    total = len(preguntas)
    correctas = 0
    resultados = []

    for i, preg in enumerate(preguntas):
        respuesta_usuario = form_data.get(f"pregunta_{i}")
        es_correcta = respuesta_usuario is not None and int(respuesta_usuario) == preg["respuesta_correcta"]
        if es_correcta:
            correctas += 1
        resultados.append({
            "pregunta": preg["pregunta"],
            "respuesta_usuario": int(respuesta_usuario) if respuesta_usuario else -1,
            "respuesta_correcta": preg["respuesta_correcta"],
            "correcta": es_correcta,
            "explicacion": preg["explicacion"],
        })

    porcentaje = round((correctas / total) * 100) if total > 0 else 0
    aprobado = porcentaje >= 70

    db = await get_db()
    await db.execute(
        "INSERT INTO resultados_test (colaborador_id, modulo_id, puntaje, total_preguntas, porcentaje, aprobado, respuestas_json) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (colaborador_id, modulo_id, correctas, total, porcentaje, 1 if aprobado else 0, json.dumps(resultados)),
    )

    # If passed, mark module as completed
    if aprobado:
        await db.execute(
            "UPDATE progreso_modulos SET completado=1, fecha_completado=datetime('now') WHERE colaborador_id=? AND modulo_id=?",
            (colaborador_id, modulo_id),
        )
    await db.commit()

    colaborador = await db.execute_fetchall(
        "SELECT * FROM colaboradores WHERE id=?", (colaborador_id,)
    )
    colaborador = colaborador[0] if colaborador else None
    await db.close()

    return templates.TemplateResponse("test_result.html", {
        "request": request,
        "colaborador": colaborador,
        "modulo": modulo,
        "resultados": resultados,
        "correctas": correctas,
        "total": total,
        "porcentaje": porcentaje,
        "aprobado": aprobado,
    })
