"""tests rivers_by_station_number function"""

from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """requirements for Task 1E"""

    # build list of stations
    stations = build_station_list()

    # print the 9 rivers that have the most stations and how many stations are on each in the form of a list of tuples
    rivers_station = rivers_by_station_number(stations, N=9)
    print("9 rivers with the most stations are: {}".format(rivers_station))


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
