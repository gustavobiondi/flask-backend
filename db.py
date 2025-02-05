from cs50 import SQL

db = SQL('sqlite:///dados.db')

db.execute('DELETE FROM pedidos')