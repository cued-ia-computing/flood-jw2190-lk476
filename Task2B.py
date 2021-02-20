from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task2B"""

    #build list of stations
    stations = build_station_list()
    update_water_levels(stations)

    #print the station sthat have a relative water level above 0.8
    print(stations_level_over_threshold(stations, 0.8))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part 1A Flood Warning System ***")
    run()
