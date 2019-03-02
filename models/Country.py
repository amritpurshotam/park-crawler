from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

Base = declarative_base()

class Country(Base):
    __tablename__ = 'Countries'

    id = Column('CountryId', Integer, primary_key=True)
    name = Column('Name', String(100))
    base_url = Column('BaseUrl', String(100))
    latitude = Column('Latitude', Float(precision=6))
    longitude = Column('Longitude', Float(precision=6))

    def __init__(self, country_dict):
        self.id = country_dict['id']
        self.name = country_dict['n']
        self.base_url = country_dict['u']
        self.latitude = country_dict['la']
        self.longitude = country_dict['lo']