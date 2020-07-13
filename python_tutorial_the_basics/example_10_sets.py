example =  set()
print(dir(example), "\n")
print(help(example.add))

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)
# Notice that data of different types can be added to the set
# Items inside the set are called elements
# Elements of a set could appear in a different order
# This is because order does not matter in a set unlike tuples and lists
# Sets do not contain duplicate elements
example.add(42)
print(example)
print(len(example))

print(help(example.remove)) # Cannot remove an element that does not exist in a set without an error
example.remove(42)
print(len(example))
print(example)

print(help(example.discard)) # Enables the user to remove an element that does not exist in a set without an error
example.discard(50)

example2 = set([28, True, 2.71828, "Helium"]) # An alternative and sometimes faster way to populate a set
print(len(example2))
example2.clear() # A faster way to empty a set (will return the empty set
print(len(example2))

# Union and intersection of sets
# Integers 1 - 10
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8, 9, 10])

print(odds.union(evens))
print(evens.union(odds))
print(odds)
print(evens)
print(odds.intersection(primes))
print(primes.intersection(evens))
print(evens.intersection(odds))
print(primes.union(composites))

print(2 in primes)
print(6 in odds)
print(9 not in evens)

print("\n", dir(primes))