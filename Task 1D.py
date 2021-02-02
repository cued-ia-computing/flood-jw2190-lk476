"""tests geo.rivers_with_station function and station_by_river function"""

from floodsystem.geo import rivers_with_station
from floodsystem.geo import station_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""

    #build list of rivers with stations
    stations = build_station_list()

    #print number of rivers with stations
    print(rivers_with_station(stations))
    print("Number of rivers: {}".format(len(rivers_with_station(stations))))

    #print the first rivers in alphabetical order
    print(rivers_with_station(stations)[:10])
    
    

if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***")
    run()
