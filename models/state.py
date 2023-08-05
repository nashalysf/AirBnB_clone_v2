#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import City
import models
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # relationship
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, detele, detele orphan')
    else:

        @property
        def cities(self):
            """getter that returns list of cities"""
            from models import storage
            city_list = []
            all_cities = storage.all(City).values()

            for city in all_cities:
                if self.id == city.state_id:
                    city_list.append(city)

            return city_list
