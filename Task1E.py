from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list

def run():
    """requirements for Task 1E"""
    rivers = []
    for stations in rivers_by_station_number(stations, 9):
        rivers.append(river.name)
    print(rivers)

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
