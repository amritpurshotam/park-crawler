from scrapers.get_runs import get_event_results, get_course_event_list
from data.db import save_all, get_by_id
from data.repository.event import get_event_without_run
from data.models import Event


#html = ''.join(open('280.html', 'r').readlines())
# results = get_event_results('https://www.parkrun.co.za/Swellendam', 5545, 280, html)
# print(len(results))
# save_all(results)

# html = ''.join(open('1725.html', 'r').readlines())
# events = get_course_event_list('https://www.parkrun.co.za/Swellendam', 1725, html)
# print(len(events))
# save_all(events)


# note to check all runs with more than 100% age grade

ids = [24041]

for id in ids:
    event = get_by_id(Event, id)
    event_id = event.id
    seq_num = event.run_sequence_number
    try:
        print('Scraping event id {}'.format(event_id))
        results = get_event_results('https://www.parkrun.co.za/Swellendam', event_id, seq_num)
        save_all(results)
    except Exception:
        print('Fetching results for event {} failed'.format(event_id))
        continue