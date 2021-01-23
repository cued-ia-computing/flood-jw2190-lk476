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
    #create unsorted list of (station,distance) tuples:
    for station in stations:
        distances.append((station.station_id,haversine(p, station.coord)))
    #sort this list based on distance, lowest to highest and return:
    return sorted_by_key(distances,1)
