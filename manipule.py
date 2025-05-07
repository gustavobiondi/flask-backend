from datetime import datetime
from cs50 import SQL
import shutil
import os


db = SQL("sqlite:///data/dados.db")

hoje = datetime.now().date()

db.execute('DROP TABLE tokens')
db.execute("INSERT INTO pagamentos (dia,faturamento, faturamento_prev, drinks, porcoes, restantes, totais_pedidos,caixinha) VALUES (?,0, 0, 0, 0, 0, 0,0)", hoje)
db.execute("CREATE TABLE IF NOT EXISTS tokens (token TEXT NOT NULL,cargo TEXT, username TEXT)")