from data.db import get_session
from models.Event import Event
from datetime import datetime

def get_by_course(course_id):
    sess = get_session()
    events = sess.query(Event).filter_by(course_id=course_id).all()
    return events

def get_last_event_number(course_id):
    sess = get_session()
    events = sess.query(Event.run_sequence_number).filter_by(course_id=course_id).all()
    return max(events)[0]

def get_last_event_date(course_id):
    events = get_by_course(course_id)
    dates = [datetime.strptime(event.date, '%d/%m/%Y' ) for event in events]
    if len(dates) == 0:
        return 0
    elif len(dates) > 0:
        return max(dates)

