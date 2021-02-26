from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit, plot_stations_on_map
from floodsystem.station import consistent_typical_range_stations, remove_latest_level_nonetype
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import flood_risk
import datetime

def run():
    """We have added a function to the submodule flood that gives a risk level for each station based on the curent 
    relative water level. We then showed the 50 stations with the highest relative water level on a map of the UK 
    and listed the current risk level of the 10 highest. We also created another function that predicts the change 
    in water level in the next 24 hours and also plots it on a map of the UK.""" 

    #build list of stations
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #clean station data
    stations = consistent_typical_range_stations(stations)
    stations = remove_latest_level_nonetype(stations)
    print(len(stations))
    
     

    #Gather the 10 stations with the highest relative water level
    highest_rellevel_stations = stations_highest_rel_level(stations,N=50)
    plot_stations_on_map(highest_rellevel_stations)
    highest_rellevel_stations = stations_highest_rel_level(stations,N=10)
    for station in highest_rellevel_stations:
        print(f'{station.town} {flood_risk(station)}')


if __name__ == "__main__":
    print("*** Task 2G: CUED Part 1A Flood Warning System ***")
    run()