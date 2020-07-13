# Alkaline earth metals

# Sorted by atomic number.
earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
print(earth_metals)

# By default the sort method assumes needs to be sorted alphabetically in ascending order.
earth_metals.sort()
print(earth_metals)

# To sort in reverse alphabetical order.
earth_metals.sort(reverse=True)
print(earth_metals)

# The sort method will not work here
# earth_metals = ("Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium")
# earth_metals.sort() # This will not work because tuples are immutable.

print(help(list.sort)) # "in-place" algorithm means a 2nd data structure is not created.

# Example: sorting the planets.
# format := (name, radius, density, distance from Sun)
# Radius: Radius at equator in kilometers
# Density: Average density in g/(cm^3)
# Distance from the Sun: Avg. distance to sun in AUs
#
# 1 Astronomical unit (AU) = Average distance of Earth to Sun

# The list is sorted by distance from the Sun.
planets = [("Mercury", 2440, 5.43, 0.395),
           ("Venus", 6052, 5.24, 0.723),
           ("Earth", 6378, 5.52, 1.000),
           ("Mars", 3396, 3.93, 1.530),
           ("Jupiter", 71492, 1.33, 5.210),
           ("Saturn", 60268, 0.69, 9.551),
           ("Uranus", 25559, 1.27, 19.213),
           ("Neptune", 24764, 1.64, 30.070),]
print("The planets sorted by distance from the Sun:")
print(planets)

# Sort the planets by size with the largest planet first.
size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print("The planets sorted by size:")
print(planets)

# Sort the planets by density starting with the least dense.
density = lambda planet: planet[2]
planets.sort(key=density)
print("The planets sorted by density:")
print(planets)

# The method list.sort() changes the list
# Q: Can you create a sorted copy?
# Q: How do you sort a tuple?
# A: Use sorted()

print(help(sorted))

earth_metals = ["Beryllium", "Magnesium", "Calcium", "Strontium", "Barium", "Radium"]
sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)
print(earth_metals)

data = (7, 2, 5, 6, 1, 3, 9, 10, 4, 8)
print(sorted(data))
print(data)

print(sorted("Alphabetical"))