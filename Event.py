from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Event(Base):
    __tablename__ = 'Events'

    event_id = Column('EventId', Integer, primary_key=True)
    name = Column('Name', String(500))
    url = Column('Url', String(500))
    latitude = Column('Latitude', Float(precision=6))
    longitude = Column('Longitude', Float(precision=6))


driver = 'SQL+Server'
username = "ParkrunUser"
password = "abc123"
host = "AMRITPU-PC"
database = "Parkrun"
connection_string = "mssql+pyodbc://{0}:{1}@{2}/{3}?driver={4}".format(username, password, host, database, driver)
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

e = Event(event_id=5, name='Test3', url='test.comasd', latitude=-26.135444, longitude=28.125331)
session.add(e)
session.commit()