from data.request import get
from bs4 import BeautifulSoup
from data.models import Event, Course, Run
from decimal import Decimal
from data.db import save_all, load_all
from data.repository.event import get_all_course_seq_num, get_event_without_run

def get_course_event_list(url, course_id):
    event_page = BeautifulSoup(get(url + "/results/eventhistory"), "html.parser")
    event_table = event_page.find_all('tbody')
    events = []
    rows = event_table[0].find_all('tr')
    runs = get_all_course_seq_num(course_id)

    for row in rows:
        aux = row.find_all('td')
        if int(aux[0].string) not in runs:
            events.append(Event({'number':aux[0].string, 'date':aux[1].string}, course_id))
    return events
    
def get_event_results(url, event_id, seq_num):
    event_page = BeautifulSoup(get(url + "/results/weeklyresults/?runSeqNumber={}".format(seq_num)), 'html.parser')
    result_table = event_page.find_all('tbody')
    results = []
    rows = result_table[0].find_all('tr')
    for row in rows:
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
            age_grade = aux[4].string
            if age_grade is not None:
                age_grade = Decimal(age_grade[:5])
            
            try:
                results.append(Run({'position': int(aux[0].string), 
                                    'id': str(hash(row.a['href'].strip("athletehistory?athleteNumber="))), 
                                    'hours':hours, 
                                    'minutes':minutes, 
                                    'seconds':seconds , 
                                    'age_category': aux[3].string, 
                                    'age_grade': age_grade,
                                    'gender': aux[5].string, 
                                    'gender_position': int(aux[6].string), 
                                    'note': aux[8].string}, event_id))
            except Exception as e:
                print(e)
                print(aux)

    return results

def get_all_event_results():
    courses = load_all(Course)
    for course in courses:
        course_id = course.id
        print("Scraping course id " + str(course_id))

        events = get_course_event_list(course.url, course_id)
        save_all(events)

        events = get_event_without_run(course_id)

        for event in events:
            event_id = event.id
            print("Scraping event " + str(event_id))
            seq_num = event.run_sequence_number
            results = get_event_results(course.url, event_id, seq_num)
            save_all(results)
