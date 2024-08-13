import importlib
from .config import DB_MODULE


db_module = importlib.import_module(DB_MODULE, "repositories")

db = getattr(db_module, 'db')
