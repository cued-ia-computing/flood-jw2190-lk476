from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task2C"""

    #build list of stations
    stations = build_station_list()

    #print the 10 stations with the highest relative water level
    water_level = stations_highest_rel_level(stations, N=10)
    print("10 stations with the highest relative water level: {}".format(water_level))

