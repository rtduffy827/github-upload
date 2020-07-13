# Fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21
# Goal: Write a function to return the nth term of the Fibonacci Sequence.
#       - Fast
#       - Clearly written
#       - Rock solid

# This is a recursive function
def fibonacci_01(n): # Follow the python style guide when writing functions
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_01(n-1) + fibonacci_01(n-2)
for n in range(1, 11): # The range function does not include the final number so this will output the first 10 terms
    print(n, ":", fibonacci_01(n))

# A good example of how recursive functions can quickly slow down a program
# for n in range(1, 101):
#    print(n, ":", fibonacci(n))
# The solution: Memoization
# The idea: Cache values (so future calls do not have to repoeat the work

# Explicit Memoization
fibonacci_cache = {}
def fibonacci_02(n):
    # If we have cached the value, then return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_02(n-1) + fibonacci_02(n-2)
    # Cache the value and return it
    fibonacci_cache[n] = value
    return value

for n in range(1, 101):
    print(n, ":", fibonacci_02(n))
#for n in range(1, 1001):
#    print(n, ":", fibonacci_02(n))

# Simpler method
from functools import lru_cache # from the functools module import a decorator called lru_cache

@lru_cache(maxsize = 1000) # The default maxsize is 128 (of the most recently used values)
def fibonacci_03(n):
    # Check that the input is a positive integer
    if type(n) != int:
        raise TypeError("n must be a positive int")
    if n < 1:
        raise ValueError("n must be a positive int")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_03(n-1) + fibonacci_03(n-2)
for n in range(1, 501):
    print(n, ":", fibonacci_03(n))
for n in range(1, 51):
    print(fibonacci_03(n+1) / fibonacci_03(n)) # The golden ratio