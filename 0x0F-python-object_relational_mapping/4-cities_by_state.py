#!/usr/bin/python3
"""
Task 4:
4-cities_by_states.py
List all cities from the database hbtn_0e_4_usa
Uses:
4-cities_by_state.sql
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
    amount = cur.execute("SELECT cities.id, cities.name, states.name \
                         FROM cities JOIN states ON cities.state_id = \
                         states.id ORDER BY cities.id;")

    for i in range(0, amount):
        results = cur.fetchone()
        print("{}".format(results))

    cur.close()
    db.close()
