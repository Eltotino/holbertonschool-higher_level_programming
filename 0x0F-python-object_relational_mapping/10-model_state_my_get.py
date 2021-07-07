#!/usr/bin/python3
"""State Module"""
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
import sys


def fetch():
    """Fetch first state in db"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search = sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
             username, password, database), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    Searched_state = session.query(State).filter_by(name=search).first()
    if Searched_state:
        print("{}".format(Searched_state.id))
    else:
        print("Not found")
    session.close()

if __name__ == "__main__":
    fetch()
