import matplotlib.pyplot as plt 
import numpy as np
from scipy.interpolate import CubicSpline
import collections
import math


ZERO_VAL_EPSILON = 0.1
MIN_BIN = 10
BASE_VALS = [1, 2, 2.5, 5]



def getBins(data):
    """Calculates a "sensible" set of bins for a set of data
    to ensure:
    - bins are a easily interpretable size
    - bins start at 0
    - histogram is smooth

    Args:
        data (array): data to find optimal histogram bins of

    Returns:
        array: set of bins
    """

    # calculate initial guess for bin size
    freedman_diaconus = freedmanDiaconus(data)

    # find powers of 10 either side of fd
    powers = []
    floor = math.floor(np.log10(freedman_diaconus))
    powers = [floor-1, floor, floor+1, floor+2]

    # initialise best bend score
    min_bend = np.inf
    min_bend_bin = None
    min_bend_count = None


    for i in powers:
        for base in BASE_VALS:
            # set bin width
            bin_width = base * 10 **i
            # calculate valuable bins
            bin_min = (min(data)//bin_width)*bin_width
            bin_max = (1+(max(data)//bin_width))*bin_width
            bins = np.arange(bin_min, bin_max + bin_width, bin_width)
            # bin the relevant data
            data_binned = np.digitize(data, bins=bins)
            bin_count = np.bincount(data_binned)
            # ensure sufficient bins are being used
            if len(bins) == len(bin_count) and len(bins)>=MIN_BIN:
                # calculate the bend energy to estimate smoothness
                bend = calculateBend(bins, bin_count)
                # if bend energy is lowest, set optimal bins
                if bend < min_bend:
                    min_bend = bend
                    min_bend_bin = bins
                    min_bend_count = bin_count

    return min_bend_bin



def freedmanDiaconus(data):
    """Calculates the Freedman Diaconus value to estimate
    a suitable width of a histogram

    Args:
        data (array): data that is being found a suitable histogram to fit to

    Returns:
        float: Freedman Diaconus value
    """
    n = len(data)
    # calculate quartiles
    x_q1, x_q3 = np.percentile(data, [25, 75])
    # calculate n data
    x_n = len(data)
    # calculate IQR
    x_iqr = x_q3 - x_q1
    # calculate Freedman Diaconus
    freedman_diaconus = 2*x_iqr*n**(-1.0/3.0)
    return freedman_diaconus
  
  
def calculateBend(x, y):
    """
    Calculates the bending energy of a set of co-ordinates using
    cubic splining to interpolate.

    Args:
        x (array): Bin values.
        y (array): Size of population in each bin.

    Returns:
        float: bend energy of set of points
    """
    # Fit a cubic spline to data and calculate second derivative
    d2y = CubicSpline(x,y).derivative().derivative()
    # Approximate integral of (d2y/dx2)^2  
    bend_energy = 0
    for i in range(1, len(x)):
        bend_energy += (d2y(x[i-1])**2 + d2y(x[i-1])*d2y(x[i]) + d2y(x[i])**2) * (x[i] - x[i-1])
    # return bend energy
    return bend_energy

def baseVals():
    return BASE_VALS

def zeroValEpsilon():
    return ZERO_VAL_EPSILON

def minBin():
    return MIN_BIN



if __name__ == "__main__":
    mu = np.random.uniform(low=-100, high = 100)
    std = np.random.uniform(low=0, high = 100)
    n = np.random.randint(5,high=10**6)
    data = np.random.gamma(std, size=(n))
    bins = getBins(data)