print(dir(), "\n")

def f():
    pass # tells python to skip this line and do nothing

f() # calls the function f()
print(f) # gives the address of the function
print("\n", dir(), "\n")

def ping(): # this function has no arguments
    return "Ping!"

print(ping())
x = ping()
print(x)
print("\n", dir(), "\n")

# Volume of a sphere = (4/3)*pi*(r^3)
import math
print(math.pi)

def volume(r):
    """Returns the volume of a a sphere with radius r."""
     # The above line is called a doc string (should contain info on what the function does and how to use it).
    v = (4.0/3.0) * math.pi * r**3 # Notice 4 and 3 are floats because in python2 as ints that division would return the quotient not the true value.
    return v

print(volume(2)) # volume must have an argument or it will get a traceback error
print(help(volume))

# Area of a triangle = (1/2) * base * height
def triangle_area(b, h):
    """Returns the area of a triangle with base b and height h."""
    return 0.5 * b * h

print(triangle_area(3, 6))

# 1 inch = 2.54 cm
# 1 foot = 12 inches
def cm(feet = 0, inches = 0): # a function with keyword or default arguments
    """Converts a length from feet and inches to centimeters."""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm

# how to call keyword functions
print(cm(feet = 5))
print(cm(inches = 70))
print(cm(feet = 5, inches = 8))
print(cm(inches = 8, feet = 5))

# Only two types of arguments when writing functions: Keyword (has an '=' sign) and Required (has no '=' sign)
# If you use both for one function then the keyword arguments must come last

def g(x, y = 0): # Required arguments are determined by their position not by their name like keyword arguments are
    return x + y

print(g(5))
print(g(7, y = 3))