from data.db import get_session
from data.models import Event, Run
from data.repository.run import count_by_event
from datetime import datetime
from sqlalchemy.sql import func

def get_by_course(course_id):
    sess = get_session()
    events = sess.query(Event).filter_by(course_id=course_id).all()
    return events

def get_all_course_seq_num(course_id):
    sess = get_session()
    ids = list(map(lambda event: event.run_sequence_number, sess.query(Event.run_sequence_number).filter_by(course_id=course_id).all()))
    return ids

def get_event_without_run(course_id):
    sess = get_session()
    events = sess.query(Event)\
                .filter_by(course_id=course_id)\
                .outerjoin(Run)\
                .group_by(Event.id, Event.course_id, Event.run_sequence_number, Event.date)\
                .having(func.count(Run.run_id)==0)\
                .order_by(Event.run_sequence_number.desc())\
                .all()
    return events