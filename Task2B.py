from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import consistent_typical_range_stations, remove_latest_level_nonetype

def run():
    """Requirements for Task2B"""

    #build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations = consistent_typical_range_stations(stations)
    stations = remove_latest_level_nonetype(stations)
    stations_over = stations_level_over_threshold(stations, 0.8)
    for station in stations_over:
        #print the station that have a relative water level above 0.8
        print(f'{station[0]} {station[1]}')
    



if __name__ == "__main__":
    print("*** Task 2B: CUED Part 1A Flood Warning System ***")
    run()
