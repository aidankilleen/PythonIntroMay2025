# sqlite_investigation.py

import sqlite3

FILE_NAME = r"C:\work\training\python\testdb.db"

with sqlite3.connect(FILE_NAME) as conn:
    cursor = conn.cursor()

    name = input ("Enter your name: ")
    email = input ("Enter your email: ")

    # parameterised query
    sql = f"INSERT INTO members (name, email, active) VALUES(?,?,?)"
    print (sql)
    cursor.execute(sql, (name, email, 0))

    sql = "SELECT * FROM members"
    cursor.execute(sql)
    rows = cursor.fetchall()

    for row in rows:
        print (row)

# CRUD 
# Create
# Retrieve
# Update
# Delete
# 
#         
