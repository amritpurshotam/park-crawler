from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Run(Base):
    __tablename__ = 'Runs'

    run_id = Column('RunId', Integer, primary_key=True)
    event_id = Column('EventId', Integer)
    parkrunner_id = Column('ParkRunnerId', Integer)
    position = Column('Position', Integer)
    hours = Column('Hours', Integer)
    minutes = Column('Minutes', Integer)
    seconds = Column('Seconds', Integer)
    age_category = Column('AgeCategory', String(7))
    age_grade = Column('AgeGrade', Float(precision=2))
    gender = Column('Gender', String(1))
    gender_position = Column('GenderPosition', Integer)
    note = Column('Note', String(20))

    def __init__(self, run_dict, event_id):
        self.event_id = event_id
        self.parkrunner_id = run_dict["id"]
        self.position = run_dict["position"]
        self.hours = run_dict["hours"]
        self.minutes = run_dict["minutes"]
        self.seconds = run_dict["seconds"]
        self.age_category = run_dict["age_category"]
        self.age_grade = run_dict["age_grade"]
        self.gender = run_dict["gender"]
        self.gender_position = run_dict["gender_position"]
        self.note = run_dict["note"]

