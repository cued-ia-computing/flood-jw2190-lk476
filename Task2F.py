from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.station import consistent_typical_range_stations, remove_latest_level_nonetype
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime

def run():
    """Requirements for Task2F"""

    #build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations = consistent_typical_range_stations(stations)
    stations = remove_latest_level_nonetype(stations)
    num_stations_toplot = 5
    highest_rellevel_stations = stations_highest_rel_level(stations,num_stations_toplot)
    dt = 2
   
    for station in highest_rellevel_stations:
        dates, levels = fetch_measure_levels(station.measure_id,datetime.timedelta(days=dt))
        #will remove any data points in levels that are not floats
        correct_levels = []
        correct_dates = []
        for pair in zip(levels,dates):
            if isinstance(pair[0],float):
                correct_levels.append(pair[0])
                correct_dates.append(pair[1])
        plot_water_level_with_fit(station, correct_dates, correct_levels, 4)            
            
        
        

if __name__ == "__main__":
    print("*** Task 2F: CUED Part 1A Flood Warning System ***")
    run()




'''
 #checks if each station actually has a water level history, and if it does not, gets highest rellevel stations again,
    #  this time getting an extra one (so that 5 are always plotted)
    def loop_if_error_found(highest_rellevel_stations):
        error_stations = 0
        for station in highest_rellevel_stations:
            dates, levels = fetch_measure_levels(station.measure_id,datetime.timedelta(days=dt))

            if len(levels) > 1: 
                print(f'number of water level points for {station.name} : {len(levels)}')
            else:
                error_stations += 1
        if len(highest_rellevel_stations) - error_stations < num_stations_toplot:
            loop_if_error_found(stations_highest_rel_level(stations,len(highest_rellevel_stations)+error_stations))
        else:
'''