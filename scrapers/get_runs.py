import re
from data.request import get
from bs4 import BeautifulSoup
from models.Event import Event
from models.Course import Course
from models.Run import Run
from decimal import Decimal
from data.db import save_all, save, load_all
from data.repository.event import load_by_course
from data.repository.course import get_by_id

def get_course_event_list(url, course_id):
    event_page = BeautifulSoup(get(url + "/results/eventhistory"), "html.parser")
    event_table = event_page.find_all('tbody')
    events = []
    for row in event_table[0].find_all('tr'):
        aux = row.find_all('td')
        #runs[aux[0].string] = {"url_ext": row.a["href"].strip(".."), "date": aux[1].string}
        events.append(Event({'number':aux[0].string, 'date':aux[1].string}, course_id))

    return events

def get_event_results(url, event_id, seq_num):
    event_page = BeautifulSoup(get(url + "/results/weeklyresults/?runSeqNumber={}".format(seq_num)), 'html.parser')
    result_table = event_page.find_all('tbody')
    results = []
    for row in result_table[0].find_all('tr'):
        aux = row.find_all('td')
        time_str = aux[2].string
        if aux[1].string == 'Unknown':
            results.append(Run({'position': aux[0].string, 'id': 0, 'hours':None, 'minutes':None, 'seconds':None , 'age_category': None, 'age_grade': None,
                                      'gender': None, 'gender_position': None, 'note': None}, event_id))
        else:
            try:
                hours=int(time_str[-7:-6])
            except:
                hours=int(0)
            minutes=int(time_str[-5:-3])
            seconds=int(time_str[-2:])
            results.append(Run({'position': int(aux[0].string), 'id': str(hash(row.a['href'].strip("athletehistory?athleteNumber="))), 'hours':hours, 'minutes':minutes, 'seconds':seconds , 'age_category': aux[3].string, 'age_grade': Decimal(aux[4].string[:5]),
                                      'gender': aux[5].string, 'gender_position': int(aux[6].string), 'note': aux[8].string}, event_id))
    return results


def get_all_event_results(): #id for each event
    courses = load_all(Course)
    # courses = []
    # courses.append(get_by_id(2236))
    # courses.append(get_by_id(2228))


    for course in courses:
        course_id = course.id
        print("Scraping course id " + course_id)

        events = get_course_event_list(course.url, course_id)
        save_all(events)

        events = load_by_course(course_id)

        for event in events:
            event_id = event.id
            print("Scraping event " + event_id)
            seq_num = event.run_sequence_number
            results = get_event_results(course.url, event_id, seq_num)
            save_all(results)


