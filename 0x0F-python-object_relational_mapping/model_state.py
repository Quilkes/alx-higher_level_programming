#!/usr/bin/python3
"""
Task 6:
model_state.py
Create a new table with the class definition of State
Uses:
6-model_state.sql
"""
from sys import argv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    A new SQL table
    """
    __tablename__ = "states"
    id = Column("id", Integer(), autoincrement=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
