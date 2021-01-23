"""tests geo.stations_by_distance function"""

from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
def run():
    """Requirements for Task 1B"""
    CamCityCentre = (52.2053, 0.1218)
    stationlist=build_station_list(use_cache=True)
    StationDistances = stations_by_distance(stationlist,CamCityCentre)
    print(f"10 closest stations: {StationDistances[:10]}")
    print(f"10 furthest stations: {StationDistances[-10:]}")


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

