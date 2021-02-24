from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import consistent_typical_range_stations, remove_latest_level_nonetype
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
import datetime
def run():
    """Requirements for Task2B"""

    #build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    stations = consistent_typical_range_stations(stations)
    stations = remove_latest_level_nonetype(stations)
    highest_rellevel_stations = stations_highest_rel_level(stations,5)
    dt = 10
    toplot = []
    for station in highest_rellevel_stations:
        dates, levels = fetch_measure_levels(station.measure_id,datetime.timedelta(days=dt))
        for level in levels:
        print(len(levels))
        toplot.append((station,dates,levels))   
    plot_water_levels(toplot)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part 1A Flood Warning System ***")
    run()
