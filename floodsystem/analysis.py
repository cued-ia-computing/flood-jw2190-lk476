
import matplotlib

import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Given the water level history for a station should compute a least-squares fit of a polynomial
    of degree p. The function should return a tuple in the form (polynomial object, change in time)"""
    x = matplotlib.dates.date2num(dates)

    y = levels

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree p
    shifted_times = [t-x[0] for t in x]
    p_coeff = np.polyfit(shifted_times, y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    return (poly, x[0])
