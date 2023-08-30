#!/usr/bin/env python3
#   Defining a persisiting a simple schema (db) using sqlAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine  # create_engine: This is a function provided by SQLAlchemy that creates a database engine. The database engine acts as the interface between your Python code and the actual database. It manages the connections and communication with the database.

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'  # give the table a name

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    engine = create_engine('sqlite:///students.db')  # sqlite:/// is just a prefix just indicates that the db about to be mentioned is an sqlite database
    Base.metadata.create_all(engine)