from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INSTANCE_DIR = BASE_DIR / "instance"
DATABASE_PATH = INSTANCE_DIR / "basedatos.db"

class Config:
    SECRET_KEY = "dev"
    DATABASE = str(DATABASE_PATH)
