from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Run(Base):
    __tablename__ = 'Runs'

    run_id = Column('RunId', Integer, primary_key=True)
    event_id = Column('EventId', Integer, ForeignKey('Events.EventId'))
    park_runner_id = Column('ParkRunnerId', Integer)
    position = Column('Position', Integer)
    minutes = Column('Minutes', Integer),
    seconds = Column('Seconds', Integer)
    age_category = Column('AgeCategory', String(2))
    age_min = Column('AgeMin', Integer)
    age_max = Column('AgeMax', Integer)
    age_grade = Column('AgeGrade', Float(precision=2))
    gender = Column('Gender', String(1))
    gender_position = Column('GenderPosition', Integer)

    event = relationship('Events', foreign_keys=[event_id])