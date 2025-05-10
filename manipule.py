from datetime import datetime, timedelta
from cs50 import SQL
import shutil
import os


var = True
if var:
    DATABASE_PATH = "/data/dados.db"
    if not os.path.exists(DATABASE_PATH):
        shutil.copy("dados.db", DATABASE_PATH)
        db = SQL("sqlite:///" + DATABASE_PATH)
else:
    db = SQL("sqlite:///data/dados.db")

hoje = datetime.now().date()

db.execute('ALTER TABLE pedidos ADD COLUMN dia TEXT')
db.execute('UPDATE pedidos SET dia = ?',hoje)