from request import get
import xml.etree.ElementTree as ET
from models.Country import Country
from models.Region import Region
from models.Course import Course
from db import get_session, add, commit

def add_country(country_dict):
    id = country_dict['id']
    name = country_dict['n']
    base_url = country_dict['u']
    latitude = country_dict['la']
    longitude = country_dict['lo']
    country = Country(id=id, name=name, base_url=base_url, latitude=latitude, longitude=longitude)
    add(country, session)

def add_region(region_dict):
    id = region_dict['id']
    country_id = region_dict['pid']
    name = region_dict['n']
    latitude = region_dict['la']
    longitude = region_dict['lo']
    region = Region(id=id, country_id=country_id, name=name, latitude=latitude, longitude=longitude)
    add(region, session)

def add_course(course_dict):
    id = course_dict['id']
    region_id = course_dict['r']
    url = "{}/{}".format('https://www.parkrun.co.za', course_dict['n'])
    name = course_dict['m']
    latitude = course_dict['la']
    longitude = course_dict['lo']
    course = Course(id=id, region_id=region_id, name=name, url=url, latitude=latitude, longitude=longitude)
    add(course, session)

result = get("https://www.parkrun.co.za/wp-content/themes/parkrun/xml/geo.xml")
tree = ET.parse(result)

region_arr = []
session = get_session()

for country in tree.getroot()[0]:
    if (country.attrib['n'] == 'South Africa'):
        add_country(country.attrib)
        for region in country:
            add_region(region.attrib)
            region_arr.append(region.attrib['id'])
        break
    
commit(session)   

index = 0
for event in tree.getroot():
    if index == 0:
        index = index + 1
        continue
    else:
        if event.attrib['r'] in region_arr:
            add_course(event.attrib)
        index = index + 1

commit(session)