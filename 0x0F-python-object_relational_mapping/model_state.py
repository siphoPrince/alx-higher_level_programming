#!/usr/bin/python3
"""
Class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Replace 'username', 'password', 'database' with your actual MySQL connection details
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost:3306/database"

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)

