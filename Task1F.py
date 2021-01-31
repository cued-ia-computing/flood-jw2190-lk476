"""tests typical_range_consistent and inconsistent_typical_range_stations"""

#from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    """Requirements for Task 1F"""
    stations = build_station_list(use_cache=True)
    # prints sorted list of all inconsistent stations in stations list
    stationnames = []
    for station in inconsistent_typical_range_stations(stations):
        stationnames.append(station.name)
    print(sorted(stationnames))


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
