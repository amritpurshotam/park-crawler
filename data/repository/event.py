from data.db import get_session
from models.Event import Event
from models.Run import Run
from data.repository.run import count_by_event
from datetime import datetime

def get_by_course(course_id):
    sess = get_session()
    events = sess.query(Event).filter_by(course_id=course_id).all()
    return events

def get_all_course_seq_num(course_id):
    sess = get_session()
    ids = list(map(lambda event: event.run_sequence_number, sess.query(Event.run_sequence_number).filter_by(course_id=course_id).all()))
    return ids

def get_event_without_run(course_id):
    events = get_by_course(course_id)
    new_event = []
    for event in events:
        runs = count_by_event(event.id)
        if runs == 0:
            new_event.append(event)

    return new_event






