import sqlite3 as db
from pathlib import Path
import os

DB_PATH = "test.db"

db_path = Path(DB_PATH)
if not db_path.exists():
	os.system('sqlite3 {} ".databases"'.format(DB_PATH))

try:
	conn = db.connect(DB_PATH)
	cur = conn.cursor()

	print (conn, cur)
except:
	print ("Error occured.")
