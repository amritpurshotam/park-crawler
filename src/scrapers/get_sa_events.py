import xml.etree.ElementTree as ET  # noqa: S405

from bs4 import BeautifulSoup

from data.db import load_all_ids, save, save_all
from data.models import Country, Course, Region
from data.request import get


# TODO: will revisit when doing Issue #3 to fix C901
def get_course_description(url):  # noqa: C901
    result = get(url)
    soup = BeautifulSoup(result, "html.parser")
    titles = soup.find_all("h2")
    description = []

    for title in titles:
        if title.contents[0] == "Course Description":
            for sibling in title.next_siblings:
                if sibling.name == "h2":
                    break
                elif sibling.name == "br":
                    continue
                elif sibling.name == "ul":
                    for item in sibling.descendants:
                        if item.string is not None:
                            stripped = str.strip(item.string)
                            if stripped != "":
                                description.append(stripped)
                elif sibling.string is not None and sibling.string != "\n":
                    description.append(str.strip(sibling.string))
    description = deduplicate(description)
    return " ".join(description)


def deduplicate(string_list):
    seen = set()
    result = []
    for item in string_list:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def run():  # noqa: C901
    result = get("https://www.parkrun.co.za/wp-content/themes/parkrun/xml/geo.xml")
    result = result.replace("\n", "")
    tree = ET.fromstring(  # noqa: S314 This whole function will be replaced in Issue #3
        result
    )

    existing_country_ids = load_all_ids(Country)
    for country_xml in tree[0]:
        if country_xml.attrib["n"] == "South Africa":
            country_id = int(country_xml.attrib["id"])
            if country_id not in existing_country_ids:
                country = Country(country_xml.attrib)
                save(country)

            existing_region_ids = load_all_ids(Region)
            regions = []
            for region in country_xml:
                region_id = int(region.attrib["id"])
                if region_id not in existing_region_ids:
                    regions.append(Region(region.attrib))
            save_all(regions)
            break

    region_ids = load_all_ids(Region)
    existing_course_ids = load_all_ids(Course)
    courses = []
    skip = True
    for course in tree:
        if skip:
            skip = False
            continue
        else:
            if course.attrib["r"] != "":
                if int(course.attrib["r"]) in region_ids:
                    course_id = int(course.attrib["id"])
                    if course_id not in existing_course_ids:
                        url = "{}/{}/course".format(
                            "https://www.parkrun.co.za", course.attrib["n"]
                        )
                        description = get_course_description(url)
                        courses.append(Course(course.attrib, description))

    save_all(courses)
