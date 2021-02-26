import matplotlib.pyplot as plt
import matplotlib.dates as mpldates
from datetime import datetime
from floodsystem.analysis import polyfit
from .flood import flood_risk, increase_rate
import numpy as np
import matplotlib.patches as mpatches

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





def percent_to_hexcol(oned_perc_change):
    """converts a percentage to a hexidecimal colour from green to red"""
    hexes = []
    for perc in oned_perc_change:
        if perc < -40: hexes.append("#118f24")
        elif perc < -20: hexes.append("#14f514")
        elif perc < -10: hexes.append("#b9f514")
        elif perc < 0: hexes.append("#edf514")
        elif perc < 10: hexes.append("#f5c114")
        elif perc < 20: hexes.append("#f57914")
        elif perc < 40: hexes.append("#f53614")
        elif perc < 60: hexes.append("#a61111")
        elif perc < 80: hexes.append("#540606")
    return hexes


def plot_stations_on_map(stations):
    """plots stations on map. Any stations with a severe flood risk warning 
    plot the name of the station on the map. Higher risks will be placed in front of lower risks on the map"""
    map_ = plt.imread("uk_map.jpg")
    plt.subplot(121)
    plt.imshow(map_, extent=[-8,1.9,50,59])
    names = []
    risk_level = []
    oned_perc_change = []
    severe_risk_coords = [[],[]]
    high_risk_coords = [[],[]]
    med_risk_coords = [[],[]]
    low_risk_coords = [[],[]]
    towns_severe_risk = []
    towns_high_risk = set()
    for station in stations:
        names.append(station.name)
        risk_level.append(flood_risk(station))
        oned_perc_change.append(increase_rate(station))
    for i in range(len(risk_level)):
        if risk_level[i] == 'severe risk':
            severe_risk_coords[0].append(stations[i].coord[1])
            severe_risk_coords[1].append(stations[i].coord[0])
            towns_severe_risk.append(stations[i].town)
        elif risk_level[i] == 'high risk':
            high_risk_coords[0].append(stations[i].coord[1])
            high_risk_coords[1].append(stations[i].coord[0])
            towns_high_risk.add(stations[i].town)
        elif risk_level[i] == 'moderate risk':
            med_risk_coords[0].append(stations[i].coord[1])
            med_risk_coords[1].append(stations[i].coord[0])
        elif risk_level[i] == 'low risk':
            low_risk_coords[0].append(stations[i].coord[1])
            low_risk_coords[1].append(stations[i].coord[0])
    plt.plot(low_risk_coords[0],low_risk_coords[1],'g.',label="Low")    
    plt.plot(med_risk_coords[0],med_risk_coords[1],'y.',label="Medium")
    plt.plot(high_risk_coords[0],high_risk_coords[1],'ro',label="High")
    plt.plot(severe_risk_coords[0],severe_risk_coords[1],'kD',label="Severe")
    plt.title(f"Flood Risk Based on Current Relative Level: {len(risk_level)} stations\nSevere risk town(s): {towns_severe_risk}")   
    plt.legend()
    colours = percent_to_hexcol(oned_perc_change)
    col_patches = [mpatches.Patch(color='#118f24',label="< -40%"),
                mpatches.Patch(color='#14f514',label="~ -20%"),
                mpatches.Patch(color='#b9f514',label="~ -10%"),
                mpatches.Patch(color='#edf514',label="~ 0%"),
                mpatches.Patch(color='#f5c114',label="~ 10%"),
                mpatches.Patch(color='#f57914',label="~ 20%"),
                mpatches.Patch(color='#f53614',label="~ 40%"),
                mpatches.Patch(color='#a61111',label="~ 60%"),
                mpatches.Patch(color='#540606',label="> 80%")]
    plt.subplot(122)
    plt.imshow(map_, extent=[-8,1.9,50,59])
    for i in range(len(colours)):
        plt.plot(stations[i].coord[1],stations[i].coord[0],color=colours[i],marker="o")    
    print(f'Severe risk towns: {towns_severe_risk}')
    print(f'High risk towns: {towns_high_risk}')
    plt.legend(handles=col_patches)
    high_per_station = stations.pop(oned_perc_change.index(max(oned_perc_change))).town
    high_per_station2 = stations.pop(oned_perc_change.index(max(oned_perc_change))).town
    high_per_station3 = stations.pop(oned_perc_change.index(max(oned_perc_change))).town
    plt.title(f"Predicted Percentage Increase in Next 24 Hours: {len(risk_level)} stations\nHighest risk towns:{high_per_station},{high_per_station2},{high_per_station3}")
    plt.show()


