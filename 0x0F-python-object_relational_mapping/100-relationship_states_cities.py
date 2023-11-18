#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco”
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    db_params = (sys.argv[1], sys.argv[2], sys.argv[3])
    engine_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(*db_params)

    engine = create_engine(engine_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    session = Session()

    california = State(name="California", cities=[City(name="San Francisco")])

    session.add(california)

    session.commit()

    session.close()
