from data.db import get_session
from models.Run import Run

def count_by_event(event_id):
    sess = get_session()
    runs = sess.query(Run).filter_by(event_id=event_id).count()
    return runs