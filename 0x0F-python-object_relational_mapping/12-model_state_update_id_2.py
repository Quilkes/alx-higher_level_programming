#!/usr/bin/python3
"""
Task 12:
12-model_state_update_id_2.py
Change the name of a State object from the database hbtn_0e_6_usa
Uses:
7-model_state_fetch_all.sql
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    sql_user = argv[1]
    sql_pass = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sql_user, sql_pass, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    results = session.query(State).all()

    for instance in results:
        if instance.id == 2:
            instance.name = "New Mexico"

    session.commit()

    session.close()
