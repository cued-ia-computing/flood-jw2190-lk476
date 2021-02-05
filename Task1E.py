"""tests rivers_by_station_number function"""

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """requirements for Task 1E"""
    
    #build list of stations
    stations = build_station_list()

    #print the rivers that have more than 9 stations on them and state how many stations are on each as a tuple
    rivers_station = rivers_by_station_number(stations, N = 10)

    print("9 rivers with the most stations are: {}".format(rivers_station))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
