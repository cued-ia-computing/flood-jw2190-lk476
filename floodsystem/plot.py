import matplotlib.pyplot as plt
import matplotlib.dates as mpldates
from datetime import datetime
from floodsystem.analysis import polyfit
import numpy as np

def plot_water_levels(station_levels_list):
    '''plots water level data and typical low and high for up to 6 different stations.
    must be fed a list of (station,dates,levels) tuples'''
    locations = [321,322,323,324,325,326]
    for entry in station_levels_list:
        station = entry[0]
        dates = entry[1]
        levels = entry[2]
        plt.subplot(locations[station_levels_list.index(entry)])
        typical_low = [station.typical_range[0]]*len(dates)
        typical_high = [station.typical_range[1]]*len(dates)
        print(dates[:20])
        dates = np.array(dates)
        plt.plot(dates,levels,label='Water Levels')
        plt.plot(dates,typical_low,label='typical low')
        plt.plot(dates,typical_high,label='typical high')
        plt.legend()
        plt.title(station.name)
        plt.xticks(rotation=20)
        plt.tight_layout(h_pad=0.00001)
    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the water level and the best fit polynomial"""
    typical_low = [station.typical_range[0]]*len(dates)
    typical_high = [station.typical_range[1]]*len(dates)

    poly_eqn, time_shift = polyfit(dates,levels,p)
    #use 50 points to plot best fit polynomial
    days_since_0001 = mpldates.date2num(dates)
    t = [x-time_shift for x in days_since_0001]
    #create plots
    plt.plot(dates, levels, label='Water Levels')
    plt.plot(dates,poly_eqn(t), label='Polynomial fit')
    plt.plot(dates,typical_low,label='typical low')
    plt.plot(dates,typical_high,label='typical high')
        
    plt.legend()
    plt.title(station.name)
    plt.xticks(rotation=20)
    plt.show()