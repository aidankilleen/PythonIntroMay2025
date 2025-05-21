# sqlite_investigation.py

import sqlite3

FILE_NAME = r"C:\work\training\python\testdb.db"

with sqlite3.connect(FILE_NAME) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    rows = cursor.fetchall()

    for row in rows:
        print (row)
