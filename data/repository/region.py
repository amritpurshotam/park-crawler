from data.db import get_session
from models.Region import Region

def get_by_id(id: int):
    sess = get_session()
    region = sess.query(Region).filter_by(id=id).first()
    return region