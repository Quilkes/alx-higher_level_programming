#!/usr/bin/python3
"""
Task 0:
0-select_states.py
Lists all states from the database hbtn_0e_0_usa
Uses:
0-select_states.sql
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    sql_user = argv[1]
    sql_pass = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sql_user,
        passwd=sql_pass,
        db=db_name
    )

    cur = db.cursor()
    amount = cur.execute("SELECT * FROM states ORDER BY states.id;")

    for i in range(amount):
        results = cur.fetchone()
        print(results)

    db.close()
