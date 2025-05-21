# sqlite_update_investigation.py

import sqlite3

FILE_NAME = r"C:\work\training\python\testdb.db"

with sqlite3.connect(FILE_NAME) as conn:
    cursor = conn.cursor()

    response = input ("Activate or deactive all users (a/d): ")

    # parameterised query
    sql = f"UPDATE members SET active=?"
    print (sql)

    # inline conditional - (ternary operator in java)
    cursor.execute(sql, (1 if response.lower().strip()[0] == 'a' else 0, ))
    print (f"{cursor.rowcount} records changed")

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
