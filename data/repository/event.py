from data.db import get_session
from models.Event import Event

def load_by_course(course_id):
    sess = get_session()
    events = sess.query(Event).filter_by(course_id=course_id).all()
    return events
