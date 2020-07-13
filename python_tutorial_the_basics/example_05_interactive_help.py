print(dir()) # Short for "directory"

print("\n", dir(__builtins__), "\n")

print(help(pow), "\n")

print(pow(2, 10))
print(2**10, "\n")

print(help(hex), "\n")
print(hex(10), "=", 0xa)

import math
print(dir())
print("\n", dir(math), "\n")

# Note print(help(radians)) will not work because the radians function lives within the math function
# Solution
print(help(math.radians))
print(math.radians(180))