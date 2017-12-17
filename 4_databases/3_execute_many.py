import sqlite3 as db
import os

DB_PATH = "test.db"

os.system("python3 2_create_database.py")

try:
	conn = db.connect(DB_PATH)
	cur = conn.cursor()

	data = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
			('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
			('2006-04-06', 'SELL', 'IBM', 500, 53.00),
		]

	cur.executemany('INSERT INTO stocks VALUES(?, ?, ?, ?, ?)', data)

	conn.commit()
finally:
	conn.close()
