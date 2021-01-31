"""tests geo.rivers_with_station function"""

from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list

def run():
    "Requirements for Task 1D"
   
    stations = build_station_list() #build station list
    rivers = []
    for river in rivers_with_station(stations):
        rivers.append(river.name)
    rivers = sorted(rivers)
    print(rivers)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***")
    run()