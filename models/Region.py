from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

Base = declarative_base()

class Region(Base):
    __tablename__ = 'Regions'

    id = Column('RegionId', Integer, primary_key=True)
    country_id = Column('CountryId', Integer)
    name = Column('Name', String(100))
    latitude = Column('Latitude', Float(precision=6))
    longitude = Column('Longitude', Float(precision=6))

    def __init__(self, region_dict):
        self.id = region_dict['id']
        self.country_id = region_dict['pid']
        self.name = region_dict['n']
        self.latitude = region_dict['la']
        self.longitude = region_dict['lo']
