#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Integer, String, Column, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    # Columns
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    # Relationships
    # DBStorage
    reviews = relationship("Review", backref='place', cascade="all, delete")
    amenities = relationship(
        'Amenity', secondary='place_amenity', viewonly=False)

    # FileStorage
    @property
    def reviews(self):
        """getter that returns list of place reviews"""
        from models import storage
        reviews_list = []
        all_reviews = storage.all(Review).values()

        for obj in all_reviews:
            if self.id == obj.place_id:
                reviews_list.append(obj)
        return all_reviews

    @property
    def amenities(self):
        """ Getter that returns list of place amenities """

        from models import storage
        amenity_list = []
        all_amenities = storage.all('Amenity').values()

        for obj in all_amenities:
            if self.id == obj.amenity_ids:
                amenity_list.append(obj)

        return amenity_list

    @amenities.setter
    def amenities(self, obj):
        """ Setter that appends amenity id """
        if isinstance(obj, 'Amenity'):
            self.amenity_id.append(obj, id)
