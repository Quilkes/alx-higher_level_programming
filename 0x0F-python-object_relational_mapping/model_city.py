#!/usr/bin/python3
"""
Task 14:
model_city.py
Create a new table with the class definition of City
Uses:
model_state.py
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """
    A new SQL table
    """
    __tablename__ = "cities"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer(), ForeignKey("states.id"), nullable=False)
