"""Database models and setup for the QA Training Platform."""
import aiosqlite
import os
from datetime import datetime

# En producción (Docker), usar volumen persistente via env var.
# En desarrollo local, usar archivo en el mismo directorio.
DB_PATH = os.environ.get(
    "DB_PATH",
    os.path.join(os.path.dirname(__file__), "training.db"),
)


async def get_db():
    """Get a database connection."""
    db = await aiosqlite.connect(DB_PATH)
    db.row_factory = aiosqlite.Row
    return db


async def init_db():
    """Initialize all database tables."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.executescript("""
            CREATE TABLE IF NOT EXISTS colaboradores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                rut TEXT UNIQUE NOT NULL,
                cargo TEXT DEFAULT 'Analista QA',
                fecha_ingreso TEXT DEFAULT (date('now')),
                activo INTEGER DEFAULT 1
            );

            CREATE TABLE IF NOT EXISTS progreso_modulos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                colaborador_id INTEGER NOT NULL,
                modulo_id TEXT NOT NULL,
                completado INTEGER DEFAULT 0,
                fecha_inicio TEXT,
                fecha_completado TEXT,
                FOREIGN KEY (colaborador_id) REFERENCES colaboradores(id),
                UNIQUE(colaborador_id, modulo_id)
            );

            CREATE TABLE IF NOT EXISTS resultados_test (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                colaborador_id INTEGER NOT NULL,
                modulo_id TEXT NOT NULL,
                puntaje INTEGER NOT NULL,
                total_preguntas INTEGER NOT NULL,
                porcentaje REAL NOT NULL,
                aprobado INTEGER NOT NULL,
                fecha TEXT DEFAULT (datetime('now')),
                respuestas_json TEXT,
                FOREIGN KEY (colaborador_id) REFERENCES colaboradores(id)
            );

            CREATE TABLE IF NOT EXISTS sesiones_calendario (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                semana INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                fecha_programada TEXT,
                duracion_min INTEGER DEFAULT 60,
                estado TEXT DEFAULT 'pendiente',
                notas TEXT
            );

            CREATE TABLE IF NOT EXISTS practicas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                colaborador_id INTEGER NOT NULL,
                modulo_id TEXT NOT NULL,
                descripcion TEXT NOT NULL,
                completada INTEGER DEFAULT 0,
                fecha_completada TEXT,
                observaciones TEXT,
                FOREIGN KEY (colaborador_id) REFERENCES colaboradores(id)
            );
        """)
        await db.commit()
