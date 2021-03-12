from data.db import get_session
from data.models import Run

def count_by_event(event_id):
    sess = get_session()
    runs = sess.query(Run).filter_by(event_id=event_id).count()
    return runs