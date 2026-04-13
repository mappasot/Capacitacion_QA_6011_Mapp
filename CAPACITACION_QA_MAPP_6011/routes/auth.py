"""Authentication routes - simple login by name/RUT."""
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    """Show login / registration page."""
    db = await get_db()
    colaboradores = await db.execute_fetchall("SELECT * FROM colaboradores WHERE activo=1 ORDER BY nombre")
    await db.close()
    return templates.TemplateResponse(request, "login.html", {"request": request, "colaboradores": colaboradores})


@router.post("/login")
async def login(request: Request, colaborador_id: int = Form(...)):
    """Log in an existing colaborador."""
    response = RedirectResponse(url=f"/dashboard/{colaborador_id}", status_code=303)
    return response


@router.post("/registro")
async def registro(request: Request, nombre: str = Form(...), rut: str = Form(...), cargo: str = Form("Analista QA")):
    """Register a new colaborador."""
    db = await get_db()
    try:
        await db.execute(
            "INSERT INTO colaboradores (nombre, rut, cargo) VALUES (?, ?, ?)",
            (nombre.strip(), rut.strip(), cargo.strip()),
        )
        await db.commit()
        cursor = await db.execute("SELECT id FROM colaboradores WHERE rut=?", (rut.strip(),))
        row = await cursor.fetchone()
        await db.close()
        return RedirectResponse(url=f"/dashboard/{row[0]}", status_code=303)
    except Exception:
        await db.close()
        return RedirectResponse(url="/?error=rut_duplicado", status_code=303)
