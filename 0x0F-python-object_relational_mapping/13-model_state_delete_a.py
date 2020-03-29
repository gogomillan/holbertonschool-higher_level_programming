#!/usr/bin/python3
"""
Module that deletes all State objects with a name containing the letter a from
the database hbtn_0e_6_usa
"""
import sys
import warnings
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


def main():
    """
    Main function for the Module
    """
    warnings.simplefilter('ignore', Warning)
    cs = 'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                     sys.argv[2], sys.argv[3])
    engine = create_engine(cs, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).filter(State.name.contains('a')).all():
        session.delete(state)

    session.commit()
    session.close()
    warnings.simplefilter('always', Warning)

if __name__ == "__main__":
    main()
