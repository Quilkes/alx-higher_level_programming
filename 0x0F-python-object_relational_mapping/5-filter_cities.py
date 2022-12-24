#!/usr/bin/python3
"""
Task 5:
5-filter_cities.py
Takes in the name of a state and
    lists all cities of that state,
    using the database hbtn_0e_4_usa
Uses:
4-cities_by_state.sql
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    sql_user = argv[1]
    sql_pass = argv[2]
    db_name = argv[3]
    name_searched = argv[4]
    list_cities = []

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
        if results[2] == name_searched:
            list_cities.append(results[1])

    for i in range(0, len(list_cities)):
        print("{}".format(list_cities[i]), end=", "
              if i < len(list_cities) - 1 else "\n")

    if len(list_cities) == 0:
        print()

    cur.close()
    db.close()
