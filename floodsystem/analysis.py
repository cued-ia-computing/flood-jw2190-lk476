
import matplotlib

import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Given the water level history for a station should compute a least-squares fit of a polynomial
    of degree p. The function should return a tuple in the form (polynomial object, change in time)"""

    x = matplotlib.dates.date2num(dates)
    polynomial = []

    for dates in x:
        y = levels
        dt = x[dates+1]-x[dates]

        # Using shifted x values, find coefficient of best-fit
        # polynomial f(x) of degree 4
        p_coeff = np.polyfit(x - x[0], y, p)

        # Convert coefficient into a polynomial that can be evaluated
        # e.g. poly(0.3)
        poly = np.poly1d(p_coeff)

        polynomial.append((poly, dt))
    
    return polynomial
