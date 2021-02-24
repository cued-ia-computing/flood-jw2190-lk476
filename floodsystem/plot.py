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

def plot_stations_on_map(stations_risks):
    map_ = plt.imread("uk_map.jpg")
    plt.imshow(map_, extent=[-5.7,1.3,50,59])
    stations, risks = zip(*stations_risks)
    print(stations)
    x_coords = []
    y_coords = []
    names = []
    risk_level = []
    for station in stations:
        x_coords.append(station.coord[1])
        y_coords.append(station.coord[0])
        names.append(station.name)
        #risk = station.flood_risk
        risk_level.append(station.flood_risk())
    for i in range(len(risk_level)):
        if risk_level[i] == 'severe risk':
            print('entered')
            plt.plot(x_coords[i],y_coords[i],'ko')
        elif risk_level[i] == 'high risk':
            plt.plot(x_coords[i],y_coords[i],'ro')
        elif risk_level[i] == 'moderate risk':
            plt.plot(x_coords[i],y_coords[i],'yo')
        elif risk_level[i] == 'low risk':
            plt.plot(x_coords[i],y_coords[i],'go')
        #plt.annotate(names[i],(x_coords[i],y_coords[i]),fontsize=7)
    print(f'risk::::: {risk_level}')
    #plt.scatter(x_coords,y_coords)
    plt.show()
