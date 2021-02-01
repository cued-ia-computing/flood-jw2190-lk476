"""tests geo.rivers_with_station function"""

from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list


def run():
    "Requirements for Task 1D"
    for station in rivers_with_station:
        print(f'len(rivers)')
        print(f'rivers[:10]')

        if river.name in ['River Aire']:
            print(station)

        if river.name in ['River Cam']:
            print(station)
        
        if river.nmae in ['River Thames']:
            print(station)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***")
    run()
