from data.db import get_session
from models.Course import Course

def get_by_region(region_id: int):
    sess = get_session()
    regions = sess.query(Course).filter_by(region_id=region_id).all()
    return regions
