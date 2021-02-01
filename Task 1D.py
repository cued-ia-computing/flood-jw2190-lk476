"""tests geo.rivers_with_station function"""

from floodsystem.geo import rivers_with_station
from floodsystem.geo import station_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""
    #build list of rivers qith stations
    rivers = rivers_with_station()
    #print number of rivers
    print("Number of rivers: {}".format(len(rivers)))


    
    for river in rivers_with_station():
        if river.name in ['River Aire']:
            print(river)

        if river.name in ['River Cam']:
            print(river)
        
        if river.nmae in ['River Thames']:
            print(river)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***")
    run()
