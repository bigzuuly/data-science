num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

from collections import Counter
import matplotlib.pyplot as plt
import math

from util.linear_algebra import sum_of_squares

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