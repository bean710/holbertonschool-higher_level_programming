#!/usr/bin/python3
"""Lists all states and their associated cities"""

if __name__ == "__main__":
    from relationship_state import State, Base
    from relationship_city import City
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

    states = session.query(State).all()

    for state in states:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
