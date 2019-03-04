import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from models.Course import Course
from data.db import load_all

def show_parkrun_locations():
    courses = load_all(Course)
    latitudes = list(map(lambda course: course.latitude, courses))
    longitudes = list(map(lambda course: course.longitude, courses))

    fig = plt.figure(figsize=(8,8))
    m = Basemap(projection='lcc', resolution='l', lat_0=-29.202114, lon_0=24.147949, width=2000000, height=1.6E6)
    m.shadedrelief()
    m.drawcoastlines()
    m.drawcountries()
    x, y = m(longitudes, latitudes)
    m.scatter(x, y, marker='.', color='g')
    plt.savefig('visualisations/parkruns.png')