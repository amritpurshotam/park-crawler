from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_session():
    driver = 'SQL+Server'
    username = "ParkrunUser"
    password = "abc123"
    host = "AMRITPU-PC"
    database = "Parkrun"
    connection_string = "mssql+pyodbc://{0}:{1}@{2}/{3}?driver={4}".format(username, password, host, database, driver)
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def add(entity, session):
    session.add(entity)

def commit(session):
    session.commit()