# sqlite_delete_investigation.py

import sqlite3

FILE_NAME = r"C:\work\training\python\testdb.db"

with sqlite3.connect(FILE_NAME) as conn:
    cursor = conn.cursor()

    name = input ("Enter name to delete: ")

    # parameterised query
    sql = f"DELETE FROM members WHERE name = ?"
    print (sql)
    cursor.execute(sql, (name,))

    if cursor.rowcount == 0:
        print (f"User {name} not found")


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
