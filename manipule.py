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
    db = SQL('sqlite:///data/dados.db')

hoje = datetime.now().date()

db.execute("DROP TABLE pagamentos")
db.execute("CREATE TABLE IF NOT EXISTS pagamentos (id INTEGER PRIMARY KEY AUTOINCREMENT, dia TEXT, valor FLOAT, forma_de_pagamento TEXT, comanda TEXT, ordem INTEGER")
print(db.execute("SELECT * FROM pagamentos"))
