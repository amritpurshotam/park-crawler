from request import get
import xml.etree.ElementTree as ET

result = get("https://www.parkrun.co.za/wp-content/themes/parkrun/xml/geo.xml")
tree = ET.parse(result)

region_arr = []

for country in tree.getroot()[0]:
    if (country.attrib['n'] == 'South Africa'):
        for region in country:
            region_arr.append(region.attrib['id'])

index = 0
for region in tree.getroot():
    if index == 0:
        index = index + 1
        continue
    else:
        if region.attrib['r'] in region_arr:
            print("{}\t{}\t{}\t{}\t{}".format(region.attrib['id'], region.attrib['n'], region.attrib['m'], region.attrib['la'], region.attrib['lo']))
        index = index + 1