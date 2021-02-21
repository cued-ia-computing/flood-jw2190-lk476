
import matplotlib

import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """Given the water level history for a station should compute a least-squares fit of a polynomial
    of degree p. The function should return a tuple in the form (polynomial object, change in time)"""

    x = matplotlib.dates.date2num(dates)

    # Create set of 10 data points on interval (1000, 1002)
    x = np.linspace(10000, 10002, 10)
    y = [0.1, 0.09, 0.23, 0.34, 0.78, 0.74, 0.43, 0.31, 0.01, -0.05]

    # Using shifted x values, find coefficient of best-fit
    # polynomial f(x) of degree 4
    p_coeff = np.polyfit(x - x[0], y, p)

    # Convert coefficient into a polynomial that can be evaluated
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))

    # Display plot
    plt.show()
