# Tuples are a smaller faster alternative to lists when dealing with ordered data

# List example
prime_numbers = [2, 3, 5, 7, 11, 13,17]

# Tuple example
perfect_squares = (1, 4,9, 16, 25, 36)

#Display lengths
print("# Primes =", len(prime_numbers))
print("# Squares =", len(perfect_squares))

# Iterate over both sequences
for p in prime_numbers:
    print("Prime:", p)
for n in perfect_squares:
    print("Square:", n)

print("List methods")
print(dir(prime_numbers))
print(80*"-")
print("Tuple methods")
print(dir(perfect_squares))
print(80*"-")

import sys
print("System methods")
print(dir(sys))
print(80*"-")
print(help(sys.getsizeof))

list_eg = [1, 2, 3, "a", "b", "c", True, 3.14159]
tuple_eg = (1, 2,3, "a", "b", "c", True, 3.14159)

print("List size =", sys.getsizeof(list_eg))
print("Tuple size =", sys.getsizeof(tuple_eg))

# Lists:
# - Add data
# - Remove data
# - Change data

# Tuples
# - Cannot be changed (i.e. Immutable)
# - Made quickly

import timeit
list_test = timeit.timeit(stmt="[1,2,3,4,5]",
                          number=1000000)
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)",
                           number=1000000)
print("List time:", list_test)
print("Tuple time:", tuple_test)

empty_tuple = ()
test1 = ("a") # This is not a tuple this is a string
test2 = ("a", "b")
test3 = ("a", "b", "c")

print(empty_tuple)
print(test1) # Prints a string
print(test2)
print(test3)

test1 = ("a",)
print(test1) # Prints a tuple

# Alternative way to create a tuple
test1 = 1,
test2 = 1, 2
test3 = 1, 2, 3

print(test1)
print(test2)
print(test3)

print(type(test1))
print(type(test2))
print(type(test3))

# Tuples with 1 Element are needed for tuple assignment
# (age, country, knows_python)
survey = (27, "Vietnam", True)

age = survey[0]
country = survey[1]
knows_python = survey[2]
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)

survey2 = (21, "Switzerland", False)
age, country, knows_python = survey2 # The number of variables must match the number of elements in the tuple or a value error will occur
print("Age =", age)
print("Country =", country)
print("Knows Python?", knows_python)