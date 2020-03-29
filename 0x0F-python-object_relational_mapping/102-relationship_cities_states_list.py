#!/usr/bin/python3
"""
Module  that lists all State objects, and corresponding City objects, contained
in the database hbtn_0e_101_usa.
"""
import sys
import warnings
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from relationship_state import State
from relationship_city import Base, City


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

    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
    warnings.simplefilter('always', Warning)

if __name__ == "__main__":
    main()
