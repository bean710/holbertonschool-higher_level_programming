#!/usr/bin/python3
"""Deletes all states with the letter a"""

if __name__ == "__main__":
    from model_state import State, Base
    from model_city import City
    from sqlalchemy import (create_engine, Table, Integer,
                            String, Column)
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    entries = session.query(City, State)\
                     .filter(State.id == City.state_id).all()

    for city, state in entries:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
