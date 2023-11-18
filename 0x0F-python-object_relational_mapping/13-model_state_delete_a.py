#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter a
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db_params = (sys.argv[1], sys.argv[2], sys.argv[3])
    engine_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(*db_params)

    engine = create_engine(engine_url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    states_delete = session.query(State).filter(State.name.like('%a%')).all()

    for state in states_delete:
        session.delete(state)
    session.commit()
