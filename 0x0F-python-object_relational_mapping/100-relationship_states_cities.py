#!/usr/bin/python3
"""
Module  that creates the State California with the City San Francisco from the
database hbtn_0e_100_usa: (100-relationship_states_cities.py)
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

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_city)
    session.commit()

    session.close()
    warnings.simplefilter('always', Warning)

if __name__ == "__main__":
    main()
