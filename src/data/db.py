import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_session():
    username = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    host = os.environ["POSTGRES_HOST"]
    database = os.environ["POSTGRES_DB"]
    connection_string = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
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
