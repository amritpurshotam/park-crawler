from db import get_session
from models.Course import Course

def get_course_urls():
    session = get_session()
    courses = session.query(Course.url).all()
    return list(map(lambda course: course.url, courses))