#!/usr/bin/python3
"""create state class and base, instance of declarative_base
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declaractive_base(metadata=mymetadata)

class State(Base):
    __tablename__ == 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
