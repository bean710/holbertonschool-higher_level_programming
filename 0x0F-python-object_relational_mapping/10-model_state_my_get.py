#!/usr/bin/python3
""" This script will list all states in the table that have a in them"""

if __name__ == "__main__":
    from model_state import State, Base
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

    state = (session.query(State).order_by(State.id)
             .filter(State.name == sys.argv[4]).first())

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
