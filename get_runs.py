import re
from data.request import get
from bs4 import BeautifulSoup
from models.Event import Event
from models.Course import Course
from models.Run import Run
from data.db import save_all, save, load_all

def get_course_event_list(url, course_id):
    event_page = BeautifulSoup(get(url + "/results/eventhistory"), "html.parser")
    event_table = event_page.find_all('tbody')
    events = []
    for row in event_table[0].find_all('tr'):
        aux = row.find_all('td')
        #runs[aux[0].string] = {"url_ext": row.a["href"].strip(".."), "date": aux[1].string}
        events.append(Event({'number':aux[0].string, 'date':aux[1].string}, course_id))

    return events

def get_event_results(url, event_id):
    event_page = BeautifulSoup(get(url + "/results/weeklyresults/?runSeqNumber={}".format(event_id)), 'html.parser')
    result_table = event_page.find_all('tbody')
    results = []
    for row in result_table[0].find_all('tr'):
        print(row)
        aux = row.find_all('td')
        time_str = aux[2].string
        if aux[1].string == 'Unknown':
            results.append(Run({'position': aux[0].string, 'id': 0, 'hours':None, 'minutes':None, 'seconds':None , 'age_category': None, 'age_grade': None,
                                      'gender': None, 'gender_position': None, 'note': None}, event_id))
        else:
            results.append(Run({'position': int(aux[0].string), 'id': hash(row.a['href'].strip("athletehistory?athleteNumber=")), 'hours':int(time_str[0:2]), 'minutes':int(time_str[3:5]), 'seconds':int(time_str[6:8]) , 'age_category': aux[3].string, 'age_grade': aux[4].string,
                                      'gender': aux[5].string, 'gender_position': int(aux[6].string), 'note': aux[8].string}, event_id))
    return results



def get_all_event_results(): #id for each event
    courses = load_all(Course)

    for course in courses:
        course_id = course.id


        events = get_course_event_list(course.url, course_id)
        save_all(events)

        for event in events:
            event_id = event.id
            results = get_event_results(course.url + "/results/weeklyresults/?runSeqNumber={}".format(event.run_sequence_number), event_id)
            save_all(results)

# events = get_course_event_list("https://www.parkrun.co.za/meyersfarm", 2236)
# save_all(events)
url = "http://www.parkrun.co.za/meyersfarm"
results = get_event_results(url, 2)
save_all(results)

















# url = "http://www.parkrun.co.za/meyersfarm/results"
# rs = get_event_results(url)
# print(rs['1'])

# url = "http://www.parkrun.co.za/meyersfarm/results/weeklyresults/?runSeqNumber=3"
# run_results = {}
# event_results = BeautifulSoup(get(url), 'html.parser')
# result_table = event_results.find_all('tbody')
# for row in result_table[0].find_all('tr'):
#     aux = row.find_all('td')
#     run_results[aux[0].string] = {'Time': aux[2].string, 'Age_Cat': aux[3].string, 'Age_Grade': aux[4].string, 'Gender': aux[5].string, 'Gender_Pos': aux[6].string}
#

# url = "http://www.parkrun.co.za/meyersfarm/results/eventhistory"
#
# event = BeautifulSoup(get(url), "html.parser")

# results = {}
# event_table = event.find_all('tbody')
# for row in event_table[0].find_all('tr'):
#     aux = row.find_all('td')
#     results[aux[0].string] = {"url_ext" :row.a["href"].strip(".."), "date": aux[1].string}
#
# print(results)


