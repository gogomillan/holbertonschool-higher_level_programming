#!/usr/bin/python3
"""
Module that that prints all City objects from the database hbtn_0e_14_usa:
"""
import sys
import warnings
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from model_state import Base
from model_state import State
from model_city import City


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

    rs = session.query(City, State).filter(City.state_id == State.id) \
                                   .order_by(City.id).all()
    for city, state in rs:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
    warnings.simplefilter('always', Warning)

if __name__ == "__main__":
    main()
