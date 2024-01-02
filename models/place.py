#!/usr/bin/python
""" A module that creates the class named Place and it's column record"""

from sqlalchemy.orm import relationship
import sqlalchemy
import models
from os import getenv
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base

if models.if_database == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id', onupdate='CASCADE',
                                            ondelete='CASCADE'),
                                 primary_key=True))


class Place(BaseModel, Base):
    """ A class named Place that defines all give column records below """

    if models.if_database == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities",
                                 viewonly=False)

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    def __init__(self, *args, **kwargs):
        """ Constructor of the class Place"""
        super().__init__(*args, **kwargs)

    if models.if_database != 'db':
        @property
        def reviews(self):
            """A custom getter method in defined to return given list"""
            from models.review import Review
            stack_review_obj = []
            total_stack_obj = models.storage.all(Review)
            for obj in total_stack_obj.values():
                if obj.place_id == self.id:
                    stack_review_obj.append(obj)
            return stack_review_obj

        @property
        def amenities(self):
            """A custom getter method in defined to return given list"""
            from models.amenity import Amenity
            stack_amn_obj = []
            total_returned_obj = models.storage.all(Amenity)
            for obj in total_returned_obj.values():
                if obj.place_id == self.id:
                    stack_amn_obj.append(obj)
            return stack_amn_obj
