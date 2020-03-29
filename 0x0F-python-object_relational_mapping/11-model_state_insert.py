#!/usr/bin/python3
"""
Module that adds the State object Louisiana to the database hbtn_0e_6_usa
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
    session = Session(engine)

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    state = session.query(State).filter_by(name='Louisiana').first()
    print("{}".format(state.id))

    session.close()
    warnings.simplefilter('always', Warning)

if __name__ == "__main__":
    main()
