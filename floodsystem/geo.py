# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine
from .utils import sorted_by_key  # noqa


def stations_by_distance(stations, p):
    """stations=list of stations, p=coord in form (lat,long)   
    Given a list of station objects and a coordinate p, this function
    returns a list of (station, distance) tuples where 'distance' (float type)
    is the distance of the station from coord p.
    """
    distances = []
    # create unsorted list of (station,distance) tuples:
    for station in stations:
        distances.append((station.name, haversine(p, station.coord)))
    # sort this list based on distance, lowest to highest and return:
    return sorted_by_key(distances, 1)


def stations_within_radius(stations, centre, r):
    """returns a list of all stations (type MonitoringStation) within a 
    radius r (km) of a given centre (lat,lon)"""
    stations_in_rad = []
    for station in stations:
        if haversine(centre, station.coord) <= r:
            stations_in_rad.append(station)
    return stations_in_rad


def rivers_with_station(stations):
    """returns a list, from a given list of station objects, of river names with a monitoring station""" 
    rivers = set() # build an empty set
    for station in stations:
        river = station.river
        rivers.add(river)
    return sorted(rivers)

def station_by_river(stations):
    """creates a dictionary that maps river names to a list of stations on a given river"""
    rivers_station = {}
    for station in stations:
        station = station
        river = station.river
        rivers_station['station'] = river
    return sorted(rivers_station)

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of monitoring stations"""
   
    numbers = []
    # create unsorted list of (river, number) tuples
    for station in stations:
        river = station.river
        numbers.append((river.name), numbers)
    