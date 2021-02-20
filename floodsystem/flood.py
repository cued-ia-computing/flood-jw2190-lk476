from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples in the form (station where water level is over tol, water level at the station).
    The list should be orderd in descending order of relative water level"""
    #create an unsorted list of tuples
    water_level = []

    for station in stations:
        if station.relative_water_level() > tol:
            water_level.append((station.name, station.relative_water_level())) 
    return sorted_by_key(water_level,1,reverse=True)
    

def stations_highest_rel_level(stations, N):
    """returns a list of N stations at which the water level relative a typical range is highest.
    The list should be order in descending order by relative level."""
    water_levels = set()
    for station in stations:
        water_level = station.relative_water_level
        water_levels.add(water_level)
        return sorted(station.relative_water_level)
