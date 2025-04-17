from datetime import datetime
from cs50 import SQL
import shutil
import os


DATABASE_PATH = "/data/dados.db"
if not os.path.exists(DATABASE_PATH):
    shutil.copy("dados.db", DATABASE_PATH)
db = SQL("sqlite:///" + DATABASE_PATH)
dia = datetime.now().date()




db.execute("UPDATE cardapio SET opcoes = ? WHERE item = ?",'Frutas(abacaxi-acai-banana com canela-caju-kiwi-limao-limao siciliano-lima da persia-manga-maracuja-melancia-morango-tangerina)Adicional(leite condensado)','item')
print(db.execute("SELECT * FROM cardapio WHERE item = 'suco'"))