
from floodsystem.station import MonitoringStation
from haversine import haversine
from floodsystem.utils import sorted_by_key

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