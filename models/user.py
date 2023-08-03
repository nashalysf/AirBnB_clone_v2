#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from models.place import Place
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""

    # creating users table
    __tablename__ = 'users'

    # creating users table columns with value specs
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", back_ref="user", cascade="all, delete")

    def __init__(self, *args, **kwargs):
        """ Inits user """
        super().__init__(*args, **kwargs)
