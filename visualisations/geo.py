import random

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

from models.Course import Course
from models.Region import Region
from data.repository.course import get_by_region, get_run_count_for_date
from data.repository.event import get_all_dates
from data.db import load_all_ids

DISTRICT_SHAPEFILE_LOCATION = 'visualisations/shapefiles/District_Municipalities_2016'

def draw_national_parkruns_with_regions():
    plt.figure(figsize=(40,40))
    m = Basemap(projection='lcc', resolution='f', lat_0=-29.202114, lon_0=24.147949, width=2000000, height=1.6E6)
    m.drawcountries()
    m.drawcoastlines()
    m.readshapefile(DISTRICT_SHAPEFILE_LOCATION, 'provinces')

    region_ids = load_all_ids(Region)
    for region_id in region_ids:
        courses = get_by_region(region_id)
        latitudes = list(map(lambda course: course.latitude, courses))
        longitudes = list(map(lambda course: course.longitude, courses))

        sizes = []
        ages = []
        r = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
        color = []
        for i in range(0, len(latitudes)):
            sizes.append(300)
            color.append(r)

        x, y = m(longitudes, latitudes)
        m.scatter(x, y, marker='.', c=color, s=sizes, alpha=0.5)

    plt.savefig('visualisations/parkruns.png')

def draw_national_parkruns(scaling_factor: float):
    dates = get_all_dates()
    for date in dates:
        d = date.date
        courses = get_run_count_for_date(d)
        plt.figure(figsize=(40,40))
        m = Basemap(projection='lcc', resolution='f', lat_0=-29.202114, lon_0=24.147949, width=2000000, height=1.6E6)
        m.drawcountries()
        m.drawcoastlines()
        m.readshapefile(DISTRICT_SHAPEFILE_LOCATION, 'provinces')

        latitudes = list(map(lambda course: course.latitude, courses))
        longitudes = list(map(lambda course: course.longitude, courses))
        runners = list(map(lambda course: course.runners/float(1.5), courses))

        x, y = m(longitudes, latitudes)
        m.scatter(x, y, marker='.', s=runners, alpha=0.5)

        filename = str(d[6:]) + str(d[3:5]) + str(d[:2]) + '.png'
        folder_name = 'visualisations/output/national_' + str(scaling_factor) + '/'
        plt.savefig(folder_name + filename, bbox_inches='tight')
        plt.close()