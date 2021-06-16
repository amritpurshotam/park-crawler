from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Country(Base):
    __tablename__ = "country"

    id = Column("id", Integer, primary_key=True)  # noqa: A003
    name = Column("name", String(100))
    base_url = Column("base_url", String(100))
    latitude = Column("latitude", Float(precision=6), nullable=False)
    longitude = Column("longitude", Float(precision=6), nullable=False)

    def __init__(self, country_dict):
        self.id = country_dict["id"]
        self.name = country_dict["n"]
        self.base_url = country_dict["u"]
        self.latitude = country_dict["la"]
        self.longitude = country_dict["lo"]


class Region(Base):
    __tablename__ = "region"

    id = Column("id", Integer, primary_key=True)  # noqa: A003
    country_id = Column("country_id", Integer, ForeignKey("country.id"), nullable=False)
    name = Column("name", String(100))
    latitude = Column("latitude", Float(precision=6), nullable=False)
    longitude = Column("longitude", Float(precision=6), nullable=False)

    def __init__(self, region_dict):
        self.id = region_dict["id"]
        self.country_id = region_dict["pid"]
        self.name = region_dict["n"]
        self.latitude = region_dict["la"]
        self.longitude = region_dict["lo"]


class Course(Base):
    __tablename__ = "course"

    id = Column("id", Integer, primary_key=True)  # noqa: A003
    region_id = Column("region_id", Integer, ForeignKey("region.id"), nullable=False)
    name = Column("name", String(100), nullable=False)
    url = Column("url", String(200), nullable=False)
    latitude = Column("latitude", Float(precision=6), nullable=False)
    longitude = Column("longitude", Float(precision=6), nullable=False)
    description = Column("description", String(8000), nullable=False)

    region = relationship("Region", foreign_keys=[region_id])

    def __init__(self, course_dict, description):
        self.id = course_dict["id"]
        self.region_id = course_dict["r"]
        self.url = "{}/{}".format("https://www.parkrun.co.za", course_dict["n"])
        self.name = course_dict["m"]
        self.latitude = course_dict["la"]
        self.longitude = course_dict["lo"]
        self.description = description


class Event(Base):
    __tablename__ = "event"

    id = Column("id", Integer, primary_key=True)  # noqa: A003
    course_id = Column("course_id", Integer, ForeignKey("course.id"), nullable=False)
    run_sequence_number = Column("run_sequence_number", Integer, nullable=False)
    date = Column("date", String(10), nullable=False)

    runs = relationship("Run")

    def __init__(self, event_dict, course_id):
        self.course_id = course_id
        self.run_sequence_number = event_dict["number"]
        self.date = event_dict["date"]


class Run(Base):
    __tablename__ = "run"

    run_id = Column("id", Integer, primary_key=True)
    event_id = Column("event_id", Integer, ForeignKey("event.id"), nullable=False)
    parkrunner_id = Column("parkrunner_id", String(50), nullable=False)
    position = Column("position", Integer, nullable=False)
    hours = Column("hours", Integer)
    minutes = Column("minutes", Integer)
    seconds = Column("seconds", Integer)
    age_category = Column("age_category", String(9))
    age_grade = Column("age_grade", Float(precision=2))
    gender = Column("gender", String(1))
    gender_position = Column("gender_position", Integer)
    note = Column("note", String(50))

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
