from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Event(Base):
    __table__ = 'Events'

    id = Column('EventId', Integer, primary_key=True)
    course_id = Column('CourseId', Integer)
    run_sequence_number = Column('RunSequenceNumber', Integer)
    date = Column('Date', Date)