from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class Event(Base):
    __tablename__ = 'Events'

    id = Column('EventId', Integer, primary_key=True)
    course_id = Column('CourseId', Integer)
    run_sequence_number = Column('RunSequenceNumber', Integer)
    date = Column('Date', String(10))

    def __init__(self, event_dict, course_id):
        self.course_id = course_id
        self.run_sequence_number = event_dict['number']
        self.date = event_dict['date']

