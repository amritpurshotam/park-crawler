from sqlalchemy.sql import func

from data.db import get_session
from data.models import Course, Event, Run


def get_by_region(region_id: int):
    sess = get_session()
    regions = sess.query(Course).filter_by(region_id=region_id).all()
    return regions


def get_by_id(course_id: int):
    sess = get_session()
    course = sess.query(Course).filter_by(id=course_id).first()
    return course


def get_run_count_for_date(date: str):
    sess = get_session()
    courses = (
        sess.query(
            Course.latitude, Course.longitude, func.count(Run.run_id).label("runners")
        )
        .join(Event)
        .filter_by(date=date)
        .join(Run)
        .group_by(Course.id, Course.latitude, Course.longitude, Event.id)
        .all()
    )
    return courses


def get_run_count_for_date_in_regions(date: str, region_ids: list):
    sess = get_session()
    courses = (
        sess.query(
            Course.latitude,
            Course.longitude,
            Course.region_id,
            func.count(Run.run_id).label("runners"),
        )
        .filter(Course.region_id.in_(region_ids))
        .join(Event, Event.course_id == Course.id)
        .filter_by(date=date)
        .join(Run)
        .group_by(
            Course.id, Course.latitude, Course.longitude, Course.region_id, Event.id
        )
        .all()
    )
    return courses
