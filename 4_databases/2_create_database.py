import sqlite3 as db
from pathlib import Path
import os

DB_PATH = "test.db"
db_path = Path(DB_PATH)

if db_path.exists():
	os.remove(DB_PATH)

os.system('sqlite3 {} ".databases"'.format(DB_PATH))

try:
	conn = db.connect(DB_PATH)
	cur = conn.cursor()

	cur.execute(''' CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real) ''')
	cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

	# Escaping user data propperly to avoid SQL Injection.
	user_inp = ('RHAT',)
	cur.execute("SELECT * FROM stocks WHERE symbol = ?", user_inp)

	conn.commit()
finally:
	conn.close()
