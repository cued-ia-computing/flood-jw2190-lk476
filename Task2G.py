from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import consistent_typical_range_stations, remove_latest_level_nonetype
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    """Requirements for Task2G"""

    #build list of stations
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #clean station data
    stations = consistent_typical_range_stations(stations)
    stations = remove_latest_level_nonetype(stations)

    """To look at the risk of flooding I have created a function that compares the current water level against 
    yesterdays water level. Then I have categorised the increase into 4 groups to show the associated risk"""

    
    