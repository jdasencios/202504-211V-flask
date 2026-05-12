import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from app import create_app
from app.db.database import get_db_connection, init_db

SEED_POSTS = [
    ("Primer post", "Contenido del primer post"),
    ("Segundo post", "Contenido del segundo post"),
]


def seed_db():
    db = get_db_connection()
    db.executemany("INSERT INTO posts (title, content) VALUES (?, ?)", SEED_POSTS)
    db.commit()


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        init_db()
        seed_db()
    print("Base de datos inicializada correctamente.")
