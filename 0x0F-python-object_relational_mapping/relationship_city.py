#!/usr/bin/python3
"""City module"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State
from sqlalchemy.orm import relationship



class City(Base):
    """City model class"""
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                )
    name = Column(String(128),
                  nullable=False
                  )
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
