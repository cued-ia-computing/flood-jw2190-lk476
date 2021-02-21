import matplotlib.pyplot as plt
from datetime import datetime

def plot_water_levels(data):
    '''plots water level data and typical low and high for up to 6 different stations.
    must be fed a list of (station,dates,levels) tuples'''
    locations = [321,322,323,324,325,326]
    for entry in data:
        station = entry[0]
        dates = entry[1]
        levels = entry[2]
        plt.subplot(locations[data.index(entry)])
        typical_low = [station.typical_range[0]]*len(dates)
        typical_high = [station.typical_range[1]]*len(dates)
        plt.plot(dates,levels,label='Water Levels')
        plt.plot(dates,typical_low,label='typical low')
        plt.plot(dates,typical_high,label='typical high')
        plt.legend()
        plt.title(station.name)
        plt.xticks(rotation=20)
        plt.tight_layout(h_pad=0.00001)
    plt.show()