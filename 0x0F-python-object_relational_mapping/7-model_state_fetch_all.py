#!/usr/bin/python3
"""State Module"""
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def fetch():
    """Fetch all states"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             username, password, database), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name,))
    session.close()

if __name__ == "__main__":
    fetch()
