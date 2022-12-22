#!/usr/bin/python3
"""
Task 1:
1-filter_states.py
List all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
Uses:
0-select_states.sql
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    sql_user = argv[1]
    sql_pass = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(
        "localhost",
        sql_user,
        sql_pass,
        db_name
    )

    cur = db.cursor()
    amount = cur.execute("SELECT id, name FROM states ORDER BY states.id;")

    for i in range(0, amount):
        results = cur.fetchone()
        if results[1][0] == 'N':
            print(results)

    cur.close()
    db.close()
