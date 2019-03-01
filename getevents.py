from request import get
import xml.etree.ElementTree as ET
from Country import Country
from Region import Region
from Course import Course
from db import get_session, add, commit

result = get("https://www.parkrun.co.za/wp-content/themes/parkrun/xml/geo.xml")
tree = ET.parse(result)

region_arr = []
session = get_session()
base_url = ''

for country in tree.getroot()[0]:
    if (country.attrib['n'] == 'South Africa'):
        id = country.attrib['id']
        name = country.attrib['n']
        base_url = country.attrib['u']
        latitude = country.attrib['la']
        longitude = country.attrib['lo']
        c = Country(id=id, name=name, base_url=base_url, latitude=latitude, longitude=longitude)
        add(c, session)
        for region in country:
            id = region.attrib['id']
            country_id = c.id
            name = region.attrib['n']
            latitude = region.attrib['la']
            longitude = region.attrib['lo']
            r = Region(id=id, country_id=country_id, name=name, latitude=latitude, longitude=longitude)
            add(r, session)
            region_arr.append(region.attrib['id'])
    
commit(session)   

index = 0
for event in tree.getroot():
    if index == 0:
        index = index + 1
        continue
    else:
        if event.attrib['r'] in region_arr:
            id = event.attrib['id']
            region_id = event.attrib['r']
            url = "{}/{}".format(base_url, event.attrib['n'])
            name = event.attrib['m']
            latitude = event.attrib['la']
            longitude = event.attrib['lo']
            course = Course(id=id, region_id=region_id, name=name, url=url, latitude=latitude, longitude=longitude)
            add(course, session)
        index = index + 1


commit(session)
