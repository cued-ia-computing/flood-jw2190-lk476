"""tests geo.rivers_with_station function and station_by_river function"""

from floodsystem.geo import rivers_with_station
from floodsystem.geo import station_by_river
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1D"""

    # build list of stations
    stations = build_station_list()

    # print number of rivers with stations
    print("Number of rivers: {}".format(len(rivers_with_station(stations))))

    # print the first rivers in alphabetical order
    print(rivers_with_station(stations)[:10])

    # print names of stations located on the different rivers in alphabetical order
    station = station_by_river(stations)

    print("Stations on the River Aire: {}".format(sorted(station['River Aire'])))

    print("Stations on the River Cam: {}".format(sorted(station['River Cam'])))

    print("Stations on the River Thames: {}".format(sorted(station['River Thames'])))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part 1A Flood Warning System ***")
    run()
