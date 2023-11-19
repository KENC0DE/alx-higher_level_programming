#!/usr/bin/python3
""" First state model
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ State clase to table"""
    __tablename__ = 'states'
    id = Column(Integer, autoincreament=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
