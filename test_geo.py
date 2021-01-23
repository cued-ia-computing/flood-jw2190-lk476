
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem.utils import sorted_by_key
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
def test_stations_by_distance():
    p = (0,0)
    #create 3 test stations:
    closest = MonitoringStation("test-s-id","test-m-id", "closest", (10,0),(10,0), "river", "town1")
    middle = MonitoringStation("test2-s-id","test2-m-id", "middle", (0,50),(0,50), "river2", "town2")
    furthest = MonitoringStation("test3-s-id","test3-m-id", "furthest", (80,80),(80,80), "river3", "town3")
    #add stations non ordered to list:
    stations = [furthest,closest,middle]
    distances = []
    for station in stations:
        distances.append((station.name,haversine(p, station.coord)))
    finaldata = sorted_by_key(distances,1)
    #checks correct list length:
    assert len(finaldata) == 3
    #checks correct order of list:
    assert finaldata[0][0] == "closest"
    assert finaldata[1][0] == "middle"
    assert finaldata[2][0] == "furthest"

def test_stations_within_radius():
    """check that the correct stations are found when
    looking at a 10km radius around Cam City Centre"""
    CamCityCentre = (52.2053, 0.1218)
    stations = build_station_list(use_cache=True)
    stationnames = []
    for station in stations_within_radius(stations, CamCityCentre, 10):
        stationnames.append(station.name)
    assert 'Bin Brook' in stationnames or 'Comberton' in stationnames or 'Oakington' in stationnames