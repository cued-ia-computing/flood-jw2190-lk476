"""tests geo.rivers_with_station function"""

from floodsystem.geo import rivers_with_station
from floodsystem.geo import station_by_river
from floodsystem.stationdata import build_station_list

def run():
    """Requirements for Task 1D"""
    #build list of rivers with stations
    stations = build_station_list()

    #print number of rivers with stations
    print("Number of rivers: {}".format(len(stations)))


    
    for river in rivers_with_station(stations):
        if river.name in ['River Aire']:
            print(river)

        if river.name in ['River Cam']:
            print(river)
        
        if river.name in ['River Thames']:
            print(river)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***")
    run()
