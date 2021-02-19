import matplotlib as plt
from datetime import datetime
def plot_water_levels(station,dates,levels):
    t = []
    for date in dates:
        t.append(datetime(date))
