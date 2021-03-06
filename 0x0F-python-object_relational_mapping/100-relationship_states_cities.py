#!/usr/bin/python3
"""Deletes all states with the letter a"""

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

    state = State(name="California")
    session.flush()
    city = City(name="San Francisco", state_id=state.id)
    state.cities.append(city)

    session.add(state)
    session.add(city)

    session.commit()
