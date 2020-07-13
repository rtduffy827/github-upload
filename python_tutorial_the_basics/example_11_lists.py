example = list()
example = []

primes = [2, 3, 5, 7, 11, 13]
primes.append(17)
primes.append(19)

print(primes)
print(primes[0])
print(primes[1])
print(primes[2])

print(primes[-1]) # Will return the last item on the list
print(primes[-2]) # Will return the second to last item on the list
print(primes[-8]) # This is as far as you can wrap around in this example because you can only wrap around the list once (i.e. primes[-9] would return an error

# Slicing a list
print(primes) # The original list.
print(primes[2:5]) # Slicing that original list
print(primes[0:6]) # Slicing only works in the range 0 to (n-1) where n is an element of the set of indecies

example = [128, True, "Alpha", 1.732, [64, False]]
print(example)

rolls = [4, 7, 2, 7, 12, 4, 7]
print(rolls) # Lists contain repeated numbers

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

print(numbers + letters) # When two lists are combined this is called concatenation
print(letters + numbers) # Order matters when concatenating

print(numbers)
print(letters)

print("\n", dir(numbers), "\n") # Use the help function to learn how to use the available operations
print(help(numbers.reverse))