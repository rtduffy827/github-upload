# Types of numbers (for python version 3.x): int, float, complex
# Types of operations (for python version 3.x): + - * /

x = 28 # int
y = 28.0 # float

print(x, type(x))
print(y, type(y))

x = float(x)
print("float(28) =", x, type(x), "\n")

w = 3.14 # float
print(w, type(w))

w = int(w)
print("int(3.14) =", w, type(w), "\n")

# jargon:
# ints are narrower than floats
# floats are wider than ints

z = 1.732 # float
print(z, type(z))
z = complex(z)
print("copmplex(1.732) =", z, type(z), "\n")

# type error: cannot convert a complex number to a float
# e.g. float(z)

# floats are narrower than complex numbers
# complex numbers are wider than floats

a = 2 # int
b = 6.0 # float
c = 12 +0j # complex number

# Rule: Python will widen numbers so they're the same type

# Addition
print("\nAddition:")
print("2 + 6.0 =", a+b, type(a+b)) # int + float

# Subtraction
print("\nSubtraction:")
print("6.0 - 2 =", b-a, type(b-a)) # float - int

# Mutiplication
print("\nMutiplication:")
print("2 * 7 =", a*7, type(a*7)) # int * int

# Division
print("\nDivision:")
print("(12 +0j) / 6.0 =", c/b, type(c/b)) # complex / float

# In python 3 an int divided by an int returns a float
# In most other programing languages this would return the quotient
print("\nDifferences in division from other languages:")
print("16 / 5 =", 16/5, type(16/5))

# Even if there is no remainder python 3 will still return a float
print("20 / 5 =", 20/5, type(20/5))

# To return the remainder when dividing use the % symbol
print("16 % 5 =", 16%5, "<the remainder>")

# To return the quotient when dividing use the // symbol
print ("16 // 5 =", 16//5, "<the quotient>")

# Remeber to avoid divide by zero errors