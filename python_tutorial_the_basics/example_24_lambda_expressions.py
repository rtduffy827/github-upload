# Lambda Expressions = Anonymous Functions

# ===== WITHOUT Anonymous Functions =====
# Write the function to compute 3x + 1.
def f(x):
    return 3*x + 1

print(f(2))

# ===== WITH Anonymous Functions =====
print(lambda x: 3*x + 1) # Lambda is not the name of the function.
                  # It is a python keyword that says what follows is an anonymous function.

# How to use an anonymous function?
# Solution 1 - Give it a name:
g = lambda x: 3*x + 1
print(g(2))

# Lambda expression with multiple inputs.
# Example: combine first name and last name into a single "Full Name".
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    leonhard", "EULER"))

# The general method for creating a Lambda Expression is to
# type the keyword lambda followed by zero or more inputs:

# lambda: "What is my purpose?"
# lambda x: 3*x+1
# lambda x, y: (x*y)**0.5 # Geometric Mean
# lambda x, y, z: (3/(1/x + 1/y + 1/z) # Harmonic Mean
#   ⋮ 
# lambda x₁, x₂, …, xₙ: <expression>

# Note lambda expressions cannot be used for multi-lined functions.

# Example of common uses of lambda expressions
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Rober Heinlein", "Arthur C. Clarke",
                 "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells",
                 "Leigh Brackett"]

print(help(scifi_authors.sort), "\n") # The key argument is a function that will be used for sorting.
                                      # Pass the key argument a lambda expression.
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

# Next use a function that makes functions.
# Example, Quadratic Functions:
# f(x) = ax2 + bx + c

def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 + bx + c"""
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)

print(f(0))
print(f(1))
print(f(2))

# Solution 2 - Never give it a name:
print(build_quadratic_function(3, 0, 1)(2)) # 3x^2 + 1 evaluated for x = 2.
# Problem is that this method is not the most readable code.

# Lamda expression are useful when you need a short throwaway function.
# Something simple that is only used once.
# Common applications are sorting and filtering data.