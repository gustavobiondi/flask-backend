from datetime import datetime
from cs50 import SQL
import shutil
import os


DATABASE_PATH = "/data/dados.db"
if not os.path.exists(DATABASE_PATH):
    shutil.copy("dados.db", DATABASE_PATH)
db = SQL("sqlite:///" + DATABASE_PATH)

hoje = datetime.now().date()

db.execute('DROP TABLE tokens')
db.execute("INSERT INTO pagamentos (dia,faturamento, faturamento_prev, drinks, porcoes, restantes, totais_pedidos,caixinha) VALUES (?,0, 0, 0, 0, 0, 0,0)", hoje)
db.execute("CREATE TABLE IF NOT EXISTS tokens (token TEXT NOT NULL,cargo TEXT, username TEXT)")