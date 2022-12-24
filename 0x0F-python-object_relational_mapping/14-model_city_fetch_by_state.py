#!/usr/bin/python3
"""
Task 14:
14-model_city_fetch_by_state.py
Print all City objects from the database hbtn_0e_14_usa
Uses:
14-model_city_fetch_by_state.sql
"""

if __name__ == "__main__":
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City

    sql_user = argv[1]
    sql_pass = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sql_user, sql_pass, db_name),
                           pool_pre_ping=True)

    Session = sessionmaker(engine)
    session = Session()
    results = session.query(City, State).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    for inst_c, inst_s in results:
        print("{}: ({}) {}".format(inst_s.name, inst_c.id, inst_c.name))

    session.close()
