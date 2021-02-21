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

    highest_rellevel_stations = stations_highest_rel_level(stations,5)
    dt = 2
    
    for station in highest_rellevel_stations:
        dates, levels = fetch_measure_levels(station.measure_id,datetime.timedelta(days=dt))
        
        plot_water_level_with_fit(station, dates, levels, 4)
        

if __name__ == "__main__":
    print("*** Task 2F: CUED Part 1A Flood Warning System ***")
    run()