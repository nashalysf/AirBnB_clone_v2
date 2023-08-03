#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """getter that returns list of cities"""
        city_list = []
        all_cities = storage.all(City).values()

        for city in all_cities:
            if self.id == city.state_id:
                city_list.append(city)

        return city_list
