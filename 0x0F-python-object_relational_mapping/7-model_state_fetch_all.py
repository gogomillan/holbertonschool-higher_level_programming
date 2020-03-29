#!/usr/bin/python3
"""
Module that lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    cs = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                     sys.argv[2], sys.argv[3])
    engine = create_engine(cs, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()

if __name__ == "__main__":
    main()
