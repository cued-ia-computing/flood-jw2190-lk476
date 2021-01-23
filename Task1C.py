"""tests geo.stations_within_radius function"""

from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def run():
    """Requirements for Task 1C"""
    CamCityCentre = (52.2053, 0.1218)
    stations = build_station_list(use_cache=True)
    stationnames = []
    for station in stations_within_radius(stations, CamCityCentre, 10):
        stationnames.append(station.name)
    stationnames = sorted(stationnames)
    print(stationnames)
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()