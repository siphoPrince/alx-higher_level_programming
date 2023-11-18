#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    db_params = (sys.argv[1], sys.argv[2], sys.argv[3])
    engine_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(*db_params)

    engine = create_engine(engine_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        statN = session.query(State).filter_by(id=city.state_id).first().name
        print('{}: ({}) {}'.format(statN, city.id, city.name))
