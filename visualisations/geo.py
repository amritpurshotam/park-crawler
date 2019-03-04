import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from models.Course import Course
from data.db import load_all
import numpy as np
import random

def show_parkrun_locations():
    courses = load_all(Course)
    latitudes = list(map(lambda course: course.latitude, courses))
    longitudes = list(map(lambda course: course.longitude, courses))
    sizes = []
    ages = []
    for i in range(0, len(latitudes)):
        sizes.append(random.randint(1, 2000) / 20)
        ages.append(random.randint(1, 400) / 4)


    m = Basemap(projection='lcc', resolution='f', lat_0=-29.202114, lon_0=24.147949, width=2000000, height=1.6E6)
    m.shadedrelief()
    m.drawcountries()
    x, y = m(longitudes, latitudes)
    m.scatter(x, y, marker='.', c=np.log10(ages), s=sizes, cmap='Greens', alpha=0.5)
    plt.savefig('visualisations/parkruns.png')