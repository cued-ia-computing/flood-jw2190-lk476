# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None
        

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        if self.typical_range == None:
            return False
        elif self.typical_range[0] < 0 or self.typical_range[1]<0:
            return False
        elif self.typical_range[0] < self.typical_range[1]:
            return True
        else:
            return False

    def relative_water_level(self):
        """returns the latest water level as a fraction of the typical range"""
        self.relative_level = None
        if self.latest_level != None: #ignores stations that have a latest level reading of None
            if self.latest_level == self.typical_range[0]:
                self.relative_level = 0
                return self.relative_level

            elif self.latest_level == self.typical_range[1]:
                self.relative_level = 1.0
                return self.relative_level

            else:
                self.relative_level = self.latest_level / self.typical_range[1]
                return self.relative_level
        else:
            print("station with latest level of None found")

    def flood_risk(self):
        """Returns the flood risk level of each station based on the relative water level"""
        if self.relative_level != None:
            if self.relative_level >= 2:
                return "severe risk"                
            elif self.relative_level >= 1 and self.relative_level < 2:
                return "high risk"               
            elif self.relative_level >= 0.75 and self.relative_level < 1:
                return "moderate risk"               
            else:
                return "low risk"
                
        
        else:
            print("Station with latest level of None found")


def inconsistent_typical_range_stations(stations):
    inconsistent = []
    for station in stations:
        if station.typical_range_consistent() == False:
            inconsistent.append(station)
    return inconsistent

def consistent_typical_range_stations(stations):
    """removes stations with inconsistent typical ranges"""
    consistent = []
    removed = 0
    for station in stations:
        if station.typical_range_consistent() == True:
            consistent.append(station)
        else: removed +=1
    print(f'inconsistent typical range stations removed: {removed}')
    return consistent

def remove_latest_level_nonetype(stations):
    """removes all stations in a list that have a latest_level of None."""
    tosend = []
    removed  = 0
    for station in stations:
        if station.latest_level != None:
            tosend.append(station)
        else: removed +=1
    print(f'latest_level of None removed: {removed}')
    return tosend
