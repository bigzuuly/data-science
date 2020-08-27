num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
daily_minutes = [1,68.77,51.25,52.08,38.36,44.54,57.13,51.4,41.42,31.22,34.76,54.01,38.79,47.59,49.1,27.66,41.03,36.73,48.65,28.12,46.62,35.57,32.98,35,26.07,23.77,39.73,40.57,31.65,31.21,36.32,20.45,21.93,26.02,27.34,23.49,46.94,30.5,33.8,24.23,21.4,27.94,32.24,40.57,25.07,19.42,22.39,18.42,46.96,23.72,26.41,26.97,36.76,40.32,35.02,29.47,30.2,31,38.11,38.18,36.31,21.03,30.86,36.07,28.66,29.08,37.28,15.28,24.17,22.31,30.17,25.53,19.85,35.37,44.6,17.23,13.47,26.33,35.02,32.09,24.81,19.33,28.77,24.26,31.98,25.73,24.86,16.28,34.51,15.23,39.72,40.8,26.06,35.76,34.76,16.13,44.04,18.03,19.65,32.62,35.59,39.43,14.18,35.24,40.13,41.82,35.45,36.07,43.67,24.61,20.9,21.9,18.79,27.61,27.21,26.61,29.77,20.59,27.53,13.82,33.2,25,33.1,36.65,18.63,14.87,22.2,36.81,25.53,24.62,26.25,18.21,28.08,19.42,29.79,32.8,35.99,28.32,27.79,35.88,29.06,36.28,14.1,36.63,37.49,26.9,18.58,38.48,24.48,18.95,33.55,14.24,29.04,32.51,25.63,22.22,19,32.73,15.16,13.9,27.2,32.01,29.27,33,13.74,20.42,27.32,18.23,35.35,28.48,9.08,24.62,20.12,35.26,19.92,31.02,16.49,12.16,30.7,31.22,34.65,13.13,27.51,33.2,31.57,14.1,33.42,17.44,10.12,24.42,9.82,23.39,30.93,15.03,21.67,31.09,33.29,22.61,26.89,23.48,8.38,27.81,32.35,23.84]

from collections import Counter
import matplotlib.pyplot as plt
import math

from util.linear_algebra import sum_of_squares
from util.linear_algebra import dot

friends_counts = Counter(num_friends)
xs = range(101)
ys = [friends_counts[x] for x in xs]
plt.bar(xs, ys)
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

print("Data Points:", len(num_friends))
print("Most Friends:", max(num_friends))
print("Least Friends:", min(num_friends))


sorted_values = sorted(num_friends)
print("Smallest Value: ", sorted_values[0])
print("Next Smallest Value: ", sorted_values[1])
print("Second Largest Value:", sorted_values[-2])

def mean(x):
  return sum(x) / len(x)

print("Mean # of Friends:", mean(num_friends))

def median(v):
  #finds the middle-most value of v
  n = len(v)
  sorted_v = sorted(v)
  midpoint = n // 2

  if n % 2 == 1:
    # if odd, return middle value
    return sorted_v[midpoint]

  else:
    #if even, return the average of the middle values
    return mean(sorted_v[midpoint - 1:midpoint])


print("Median: ", median(num_friends))

def quantile(x, p):
  #returns the pth - percentile value in x
  p_index = int(p * len(x))
  return sorted(x)[p_index]

print("10% Quantile: ", quantile(num_friends, 0.10))
print("90% Quantile: ", quantile(num_friends, 0.90))

def mode(x):
  #returns a list of most common values, might be more than one value
  counts = Counter(x)
  max_count = max(counts.values())

  return [x_i for x_i, count in counts.items()
    if count == max_count]

print("Most Friends: ", mode(num_friends))

def data_range(x):
  return max(x) - min(x)

print("Data Range: ", data_range(num_friends))

def de_mean(x):
  # translate x by subtracting its mean (so the result has mean 0)
  x_bar = mean(x)

  return [x_i - x_bar for x_i in x]

def variance(x):
  # assumes x has at least 2 elements
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1)

print("Variance: ", variance(num_friends))

def standard_deviation(x):
  return math.sqrt(variance(x))

print("Standard Deviation: ", standard_deviation(num_friends))

def interquantile_range(x):
  return quantile(x, 0.75) - quantile(x, 0.25)

print("Interquantile Range: ", interquantile_range(num_friends))

def covariance(x, y):
  n = len(x)
  return dot(de_mean(x), de_mean(y)) / (n - 1)

print("Covariance: ", covariance(num_friends, daily_minutes))

def correlation(x, y):
    # Measures how much x and y vary in tandem about their means
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0    # if no variation, correlation is zero

print("Correlation: ", correlation(num_friends, daily_minutes))

outlier = num_friends.index(100)    # index of outlier
num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

daily_minutes_good = [x
                      for i, x in enumerate(daily_minutes)
                      if i != outlier]

print("Correlation without outlier: ", correlation(num_friends_good, daily_minutes_good))

