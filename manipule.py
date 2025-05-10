from datetime import datetime, timedelta
from cs50 import SQL
import shutil
import os



DATABASE_PATH = "/data/dados.db"
if not os.path.exists(DATABASE_PATH):
    shutil.copy("dados.db", DATABASE_PATH)
db = SQL("sqlite:///" + DATABASE_PATH)

hoje = datetime.now().date()

db.execute('ALTER TABLE pedidos ADD COLUMN dia TEXT')
db.execute('UPDATE pedidos SET dia = ?',hoje)