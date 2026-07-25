#!/usr/bin/python3
"""Defines the State class with relationship."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class State(Base):
    """Represents the states table."""

    __tablename__ = "states"

    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )

    name = Column(
        String(128),
        nullable=False
    )

    cities = relationship(
        "City",
        back_populates="state",
        cascade="all, delete"
    )
