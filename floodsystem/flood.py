from .utils import sorted_by_key
from floodsystem.datafetcher import fetch_measure_levels
import datetime
from floodsystem.analysis import polyfit
import matplotlib.dates as mpldates
def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples in the form (station where water level is over tol, water level at the station).
    The list should be orderd in descending order of relative water level"""
    #create an unsorted list of tuples
    water_level = []

    for station in stations:
        if station.relative_water_level() > tol:
            water_level.append((station.name, station.relative_water_level())) 
    return sorted_by_key(water_level,1,reverse=True)
    

def stations_highest_rel_level(stations, N):
    """returns a list of N stations at which the water level relative a typical range is highest.
    The list should be order in descending order by relative level."""
    stations_tosend = []
    relative_levels = []
    for station in stations:
        relative_levels.append((station,station.relative_water_level()))
    relative_levels = sorted_by_key(relative_levels,1,reverse=True)
    for i in range(N):
        stations_tosend.append(relative_levels[i][0])
    return stations_tosend


def flood_risk(station):
        """Returns the flood risk level of each station based on the relative water level"""
        if hasattr(station,'relative_level'):
            if station.relative_level != None:
                if station.relative_level >= 2:
                    return "severe risk"                
                elif station.relative_level >= 1 and station.relative_level < 2:
                    return "high risk"               
                elif station.relative_level >= 0.75 and station.relative_level < 1:
                    return "moderate risk"               
                else:
                    return "low risk"

            else:
                print("Station with latest level of None found")



def increase_rate(station):
    """returns the expected percentage increase in water level 
    in the next day based on a 5th order hyperbolic approximation using the last 10 days of data"""
    print(f"predicting: {station.name}")
    dt = 10
    dates, levels = fetch_measure_levels(station.measure_id,datetime.timedelta(days=dt))
    if len(levels) == 0:
        return 0
    correct_levels = []
    correct_dates = []
    removed = 0
    for level in levels:
        if isinstance(level,float):
            correct_levels.append(level)
            correct_dates.append(dates[levels.index(level)])
        else:
            removed+=1
    if removed > 0:
        print(f"{removed} error points out of {len(levels)} removed for {station.name}")
    poly_eqn, time_shift = polyfit(correct_dates,correct_levels,5)
    
    today_since_0001 = mpldates.date2num(dates[-1])
    ten_days_ago_0001 =  mpldates.date2num(dates[0])
    level_today = poly_eqn(today_since_0001-ten_days_ago_0001)
    level_tomorrow = poly_eqn(today_since_0001-ten_days_ago_0001+1)
    return (100*(level_tomorrow-level_today)/level_today)