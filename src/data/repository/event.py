from sqlalchemy.sql import func

from data.db import get_session
from data.models import Event, Run


def get_by_course(course_id):
    sess = get_session()
    events = sess.query(Event).filter_by(course_id=course_id).all()
    return events


def get_all_course_seq_num(course_id):
    sess = get_session()
    ids = list(
        map(
            lambda event: event.run_sequence_number,
            sess.query(Event.run_sequence_number).filter_by(course_id=course_id).all(),
        )
    )
    return ids


def get_events_without_run(course_id):
    sess = get_session()
    events = (
        sess.query(Event)
        .filter_by(course_id=course_id)
        .outerjoin(Run)
        .group_by(Event.id, Event.course_id, Event.run_sequence_number, Event.date)
        .having(func.count(Run.run_id) == 0)
        .order_by(Event.run_sequence_number.desc())
        .all()
    )
    return events


def get_all_dates():
    sess = get_session()
    dates = sess.query(Event.date).distinct().all()
    return dates
