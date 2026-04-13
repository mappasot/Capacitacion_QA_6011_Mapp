"""Capacitación QA - Plataforma de entrenamiento interactivo.

Plataforma de nivelación de conocimientos teóricos y prácticos
para el equipo de Quality Assurance del CD Quilicura.
"""
import asyncio
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from database import init_db
from routes.auth import router as auth_router
from routes.modules import router as modules_router
from routes.admin import router as admin_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize database on startup."""
    await init_db()
    yield


app = FastAPI(
    title="Capacitación QA - Walmart Chile",
    description="Plataforma de nivelación de conocimientos del área QA",
    lifespan=lifespan,
)

app.include_router(auth_router)
app.include_router(modules_router)
app.include_router(admin_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8501, reload=True)
