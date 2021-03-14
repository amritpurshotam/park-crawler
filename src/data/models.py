from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Country(Base):
    __tablename__ = "Countries"

    id = Column("CountryId", Integer, primary_key=True)  # noqa: A003
    name = Column("Name", String(100))
    base_url = Column("BaseUrl", String(100))
    latitude = Column("Latitude", Float(precision=6))
    longitude = Column("Longitude", Float(precision=6))

    def __init__(self, country_dict):
        self.id = country_dict["id"]
        self.name = country_dict["n"]
        self.base_url = country_dict["u"]
        self.latitude = country_dict["la"]
        self.longitude = country_dict["lo"]


class Region(Base):
    __tablename__ = "Regions"

    id = Column("RegionId", Integer, primary_key=True)  # noqa: A003
    country_id = Column("CountryId", Integer, ForeignKey("Countries.CountryId"))
    name = Column("Name", String(100))
    latitude = Column("Latitude", Float(precision=6))
    longitude = Column("Longitude", Float(precision=6))

    def __init__(self, region_dict):
        self.id = region_dict["id"]
        self.country_id = region_dict["pid"]
        self.name = region_dict["n"]
        self.latitude = region_dict["la"]
        self.longitude = region_dict["lo"]


class Course(Base):
    __tablename__ = "Courses"

    id = Column("CourseId", Integer, primary_key=True)  # noqa: A003
    region_id = Column("RegionId", Integer, ForeignKey("Regions.RegionId"))
    name = Column("Name", String(100))
    url = Column("Url", String(200))
    latitude = Column("Latitude", Float(precision=6))
    longitude = Column("Longitude", Float(precision=6))
    description = Column("Description", String(2000))

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
    __tablename__ = "Events"

    id = Column("EventId", Integer, primary_key=True)  # noqa: A003
    course_id = Column("CourseId", Integer, ForeignKey("Courses.CourseId"))
    run_sequence_number = Column("RunSequenceNumber", Integer)
    date = Column("Date", String(10))

    runs = relationship("Run")

    def __init__(self, event_dict, course_id):
        self.course_id = course_id
        self.run_sequence_number = event_dict["number"]
        self.date = event_dict["date"]


class Run(Base):
    __tablename__ = "Runs"

    run_id = Column("RunId", Integer, primary_key=True)
    event_id = Column("EventId", Integer, ForeignKey("Events.EventId"))
    parkrunner_id = Column("ParkRunnerId", String(50))
    position = Column("Position", Integer)
    hours = Column("Hours", Integer)
    minutes = Column("Minutes", Integer)
    seconds = Column("Seconds", Integer)
    age_category = Column("AgeCategory", String(9))
    age_grade = Column("AgeGrade", Float(precision=2))
    gender = Column("Gender", String(1))
    gender_position = Column("GenderPosition", Integer)
    note = Column("Note", String(50))

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
