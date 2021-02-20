from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import consistent_typical_range_stations, remove_latest_level_nonetype

def run():
    """Requirements for Task2C"""

    #build list of stations
    stations = build_station_list()
    #update water levels
    update_water_levels(stations)
    #clean station data
    stations = consistent_typical_range_stations(stations)
    stations = remove_latest_level_nonetype(stations)
    #get the 10 stations with the highest relative water level
    highest_rel_stations = stations_highest_rel_level(stations, N=10)
    for station in highest_rel_stations:
        print(f'{station[0].name} {station[1]}')


if __name__ == "__main__":
    print("*** Task 2C: CUED Part 1A Flood Warning System ***")
    run()