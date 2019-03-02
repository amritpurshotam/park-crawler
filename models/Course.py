from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Course(Base):
    __tablename__ = 'Courses'

    id = Column('CourseId', Integer, primary_key=True)
    region_id = Column('RegionId', Integer)
    name = Column('Name', String(100))
    url = Column('Url', String(200))
    latitude = Column('Latitude', Float(precision=6))
    longitude = Column('Longitude', Float(precision=6))
    description = Column('Description', String(2000))

    def __init__(self, course_dict, description):
        self.id = course_dict['id']
        self.region_id = course_dict['r']
        self.url = "{}/{}".format('https://www.parkrun.co.za', course_dict['n'])
        self.name = course_dict['m']
        self.latitude = course_dict['la']
        self.longitude = course_dict['lo']
        self.description = description