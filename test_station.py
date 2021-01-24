# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():
    consistent = MonitoringStation("test-s-id","test-m-id", "consistent", (10,0),(0,10), "river", "town1")
    inconsistent = MonitoringStation("test2-s-id","test2-m-id", "inconsistent", (0,50),(100,0), "river2", "town2")
    inconsistent2 = MonitoringStation("test3-s-id","test3-m-id", "inconsistent2", (80,80),None, "river3", "town3")
    stations = [consistent,inconsistent,inconsistent2]
    inconsistentstations = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistentstations.append(station)
    assert not "consistent" in inconsistentstations