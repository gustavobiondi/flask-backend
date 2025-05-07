from datetime import datetime
from cs50 import SQL
import shutil
import os


DATABASE_PATH = "/data/dados.db"
if not os.path.exists(DATABASE_PATH):
    shutil.copy("dados.db", DATABASE_PATH)
db = SQL("sqlite:///" + DATABASE_PATH)

hoje = datetime.now().date()

