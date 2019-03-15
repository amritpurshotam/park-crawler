import os, random

import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.basemap import Basemap
import numpy as np

from data.models import Course, Region
from data.repository.course import get_by_region, get_run_count_for_date, get_run_count_for_date_in_regions, get_run_count_for_date_in_regions
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

def draw_gauteng(height, width, size, scaling_factor):
    dates = get_all_dates()
    region_ids = [34, 35, 57, 78, 79, 83]
    colour_dict = {}
    cmap = matplotlib.cm.get_cmap('tab10')
    for i in range(len(region_ids)):
        colour_dict[region_ids[i]] = cmap(float(i)/len(region_ids))[:3]

    for date in dates:
        date = date.date
        courses = get_run_count_for_date_in_regions(date, region_ids)

        plt.figure(figsize=(size, size))
        m = Basemap(projection='lcc', resolution='f', lat_0=-26.206121, lon_0=27.953589, width=width, height=height)
        m.drawcountries()
        m.drawcoastlines()
        m.readshapefile(DISTRICT_SHAPEFILE_LOCATION, 'provinces')

        latitudes = list(map(lambda course: course.latitude, courses))
        longitudes = list(map(lambda course: course.longitude, courses))
        runners = list(map(lambda course: course.runners * scaling_factor, courses))
        c = list(map(lambda course: colour_dict[course.region_id], courses))

        plt.text(6000, 140000, date, fontsize=40)
        x, y = m(longitudes, latitudes)
        m.scatter(x, y, marker='.', c=c, cmap='tab10', s=runners, alpha=0.5)

        filename = str(date[6:]) + str(date[3:5]) + str(date[:2]) + '.png'
        folder_name = 'visualisations/output/gauteng/'
        plt.savefig(folder_name + filename, bbox_inches='tight')
        plt.close()

def rename_for_ffmpeg(path: str):
    path = 'C:/Development/park-crawler/visualisations/output/gauteng - Copy'
    filenames = os.listdir(path)
    filenames.sort()

    i = 1
    for filename in filenames:
        os.rename(path + '/' + filename, path + '/' + str(i) + '.png')
        i = i + 1