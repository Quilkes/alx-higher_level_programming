#!/usr/bin/python3
"""
Task 2:
2-filter_states.py
Takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa
    where name matches the argument
Uses:
0-select_states.sql
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    sql_user = argv[1]
    sql_pass = argv[2]
    db_name = argv[3]
    name_searched = argv[4]

    db = MySQLdb.connect(
        "localhost",
        sql_user,
        sql_pass,
        db_name
    )

    cur = db.cursor()
    amount = cur.execute("SELECT * FROM states ORDER BY states.id;")

    for i in range(0, amount):
        results = cur.fetchone()
        if results[1] == name_searched:
            print("{}".format(results))

    cur.close()
    db.close()
