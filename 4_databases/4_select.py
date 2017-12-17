import sqlite3 as db
import os

DB_PATH = "test.db"

os.system("python3 3_execute_many.py")

try:
	conn = db.connect(DB_PATH)
	cur = conn.cursor()

	# can use cur as iterator after select
	cur.execute("SELECT * FROM stocks")
	for row in cur:
		print (row)

	# fetch one row at a time
	cur.execute("SELECT * FROM stocks WHERE price > 50")
	row = cur.fetchone()
	while row:
		print(row)
		row = cur.fetchone()
finally:
	conn.close()
