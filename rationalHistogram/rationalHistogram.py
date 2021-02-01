import matplotlib.pyplot as plt 
import numpy as np
from scipy.interpolate import CubicSpline
import collections
import math


OVERFLOW_EPSILON = 0.01
ZERO_VAL_EPSILON = 0.1
MIN_BIN = 10
BASE_VALS = [1, 2, 2.5, 5]



def getBins(data):

  freedman_diaconus = freedmanDiaconus(data)

  powers = []
  floor = math.floor(np.log10(freedman_diaconus))
  powers = [floor-1, floor, floor+1, floor+2]

  min_bend = np.inf
  min_bend_bin = None
  min_bend_count = None


  for i in powers:
    for base in BASE_VALS:
      bin_width = base * 10 **i
      bin_min = (min(data)//bin_width)*bin_width
      bin_max = (1+(max(data)//bin_width))*bin_width
      bins = np.arange(bin_min, bin_max + bin_width, bin_width)
      data_binned = np.digitize(data, bins=bins)
      bin_count = np.bincount(data_binned)

      if len(bins) == len(bin_count) and len(bins)>MIN_BIN:
        bend = calculateBend(bins, bin_count)
        if bend < min_bend:
          min_bend = bend
          min_bend_bin = bins
          min_bend_count = bin_count

  return min_bend_bin, min_bend_count, min_bend



def freedmanDiaconus(data):
  x_q1, x_q3 = np.percentile(data, [25, 75])
  x_n = len(data)
  x_iqr = x_q3 - x_q1
  freedman_diaconus = 2*x_iqr*(n**(-1/3))
  return freedman_diaconus
  
  
def calculateBend(x, y):

  d2y = CubicSpline(x,y).derivative().derivative()
  bend_energy = 0
  for i in range(1, len(x)):
    bend_energy += (d2y(x[i-1])**2 + d2y(x[i-1])*d2y(x[i]) + d2y(x[i])**2) * (x[i] - x[i-1])
  return bend_energy




if __name__ == "__main__":
    mu = np.random.uniform(low=-100, high = 100)
    std = np.random.uniform(low=0, high = 100)
    n = np.random.randint(5,high=10**6)
    data = np.random.gamma(std, size=(n))
    x, y, bend = getBins(data)