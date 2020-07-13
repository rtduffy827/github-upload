
# The map, filter, and reduce functions help manipulate lists.

# ===== The map function =====
import math

def area(r):
    """Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5, 7.1, 0.3, 10]

# Method 1: Direct method.
areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

# Method 2: Use 'map' function.
# map(<function>, <iterable object>) {i.e. list, tuple, ect…}
map_object = map(area, radii) # The function map will apply the area function to every element in the list.
                              # A list and tuple are examples of iterable objects.
                              # The function map(<function>, <iterable object>) returns a map object.
                              # A map object is an iterator over the results, which is desirable for large data sets.
print(map_object)

areas = list(map_object) # Turn the map object into a list by passing it into the list constructor.
print(areas)

# Example: Suppose a weather company records the temperature of various cities around to world in degrees Celsius,
# but a consumer wants those temperatures in degrees Fahrenheit.
# F = (9/5)*C + 32
temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19),
         ("Los Angeles", 26), ("Tokyo", 27), ("New York", 28),
         ("London", 22), ("Beijin", 32)]

c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)

print(list(map(c_to_f, temps)))

# ===== The filter function =====
# Example: Suppose all data above the average needs to be found.
import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print(avg)

above_avg = filter(lambda x: x > avg, data) # The function filter(<function>, <set of data>) returns a filter object.
                                            # A filter object is an iterator over the results, which is desirable for large data sets.
print(list(above_avg))

# For all data below the average.
print(list(filter(lambda x: x < avg, data)))

# Remove all missing data
countries = ["", "Argentina", "", "Brazil", "Chile", "", "Colombia", "",
             "Ecuador", "", "", "Venezuela"]
# False values: "", 0, 0.0, 0j, [], (), {}, False, None, instances which signal they are empty.
# Be careful when filtering with false values. 0 is often a valid peice of data.
print(list(filter(None, countries)))

# ===== The reduce function =====
# In python 3+, reduce is not a builtin function.
# Moved to the 'functools' module.
# "Use functools.reduce() if you really need it; however,
# 99% of the time an explicit for loop is more readable."
# - Guido van Rossum (Python creator)

# Data: [a_1, a_2, a_3, ..., a_n]
# Function: f(x, y)

# reduce(f, data):
#     Step 1: val_1 = f(a_1, a_2)
#     Step 2: val_2 = f(val_1, a_3)
#     Step 3: val_3 = f(val_2, a_4)
#     ⋮
#     Step n-1: val_n-1 = f(val_n-2, a_n)
#     return val_n-1
#
# Alternatively:
#     Returns f(...f(f(f(a_1, a_2), a_3), a_4, ..., a_n)
from functools import reduce

# Multiply all numbers in a list.

# Using reduce
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x*y
print(reduce(multiplier, data))

# Using a 'for' loop
product = 1
for x in data:
    product = product * x

print(product)