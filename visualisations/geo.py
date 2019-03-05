import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from models.Course import Course
from models.Region import Region
from data.repository.course import get_by_region
from data.db import load_all_ids
import numpy as np
import random

def show_parkrun_locations():
    plt.figure(figsize=(40,40))
    m = Basemap(projection='lcc', resolution='f', lat_0=-29.202114, lon_0=24.147949, width=2000000, height=1.6E6)
    m.drawcountries()
    m.drawcoastlines()
    m.readshapefile('visualisations/shapefiles/District_Municipalities_2016', 'provinces')

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