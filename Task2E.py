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
        #will remove any data points in levels that are not floats
        correct_levels = []
        correct_dates = []
        removed = 0
        for pair in zip(levels,dates):
            if isinstance(pair[0],float):
                correct_levels.append(pair[0])
                correct_dates.append(pair[1])
            else:
                removed+=1
        if removed > 0:
            print(f"{removed} error points out of {len(levels)} removed for {station.name}")
        toplot.append((station,correct_dates,correct_levels))   
    plot_water_levels(toplot)



if __name__ == "__main__":
    print("*** Task 2E: CUED Part 1A Flood Warning System ***")
    run()
