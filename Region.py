from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Region(Base):
    __tablename__ = 'Regions'

    id = Column('RegionId', Integer, primary_key=True)
    country_id = Column('CountryId', Integer, ForeignKey('Countries.CountryId'))
    name = Column('Name', String(100))
    latitude = Column('Latitude', Float(precision=6))
    longitude = Column('Longitude', Float(precision=6))

    country = relationship('Countries', foreign_keys=[country_id])
