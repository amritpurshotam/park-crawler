from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    driver = "SQL+Server"
    username = "ParkrunUser"
    password = "abc123"  # noqa: S105
    host = "(local)"
    database = "Parkrun"
    connection_string = "mssql+pyodbc://{0}:{1}@{2}/{3}?driver={4}".format(
        username, password, host, database, driver
    )
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def load_all(entity):
    sess = get_session()
    entities = sess.query(entity).all()
    return entities


def load_all_ids(entity):
    sess = get_session()
    ids = list(map(lambda entity: entity.id, sess.query(entity.id).all()))
    return ids


def get_by_id(entity, entity_id):
    sess = get_session()
    return sess.query(entity).get(entity_id)


def save(entity):
    sess = get_session()
    sess.add(entity)
    sess.commit()


def save_all(entities):
    sess = get_session()
    for entity in entities:
        sess.add(entity)
    sess.commit()
