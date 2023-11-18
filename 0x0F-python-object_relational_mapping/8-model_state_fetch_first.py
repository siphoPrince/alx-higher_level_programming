#!/usr/bin/python3
"""lists all State objects
    from the database hbtn_0e_6_usa"""
import sys
import sqlalchemy
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def all_state(State):
    """lists all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database_name), pool_pre_ping=True)
    s = Session(engine)
    result =  s.query(State).order_by(State.id).first()
    if result is None:
        print("Nothing")
    else:
        print(f"{result.id}: {result.name}")
    s.close()


if __name__ == "__main__":
    all_state(State)

