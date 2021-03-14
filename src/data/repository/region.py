from data.db import get_session
from data.models import Region


def get_by_id(region_id: int):
    sess = get_session()
    region = sess.query(Region).filter_by(id=region_id).first()
    return region
