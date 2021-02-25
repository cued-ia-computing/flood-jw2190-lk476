from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit, plot_stations_on_map
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
    print(len(stations))
    
    """I have added a function to station so that it gives a risk level for each station based of 
    the relative water level"""  

    #Gather the 10 stations with the highest relative water level
    highest_rellevel_stations = stations_highest_rel_level(stations,N=1900)
    plot_stations_on_map(highest_rellevel_stations)
    highest_rellevel_stations = stations_highest_rel_level(stations,N=10)
    for station in highest_rellevel_stations:
        print(f'{station.town} {station.flood_risk()}')


if __name__ == "__main__":
    print("*** Task 2G: CUED Part 1A Flood Warning System ***")
    run()