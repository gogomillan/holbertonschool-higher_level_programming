#!/usr/bin/python3
"""
Module that prints the first State object from the database hbtn_0e_6_usa
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

    state = session.query(State).filter_by(name=sys.argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
    warnings.simplefilter('always', Warning)

if __name__ == "__main__":
    main()
