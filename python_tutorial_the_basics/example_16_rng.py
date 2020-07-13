# WARNING: The pseudo-random generators of this module should not be used for security purposes.
# Use ox.urando() or SystemRandom if you require a cryptographical secure pseudo-random number genereator
import random
print(dir(random), "\n")
print(help(random.random))

# Display 10 random numbers from interval [0, 1)
print("\nUniform distribution in the interval [0, 1)")
for i in range(10):
    print(random.random())

# One way to generate random numbers from interval [3, 7)
def my_random():
    # Random, scale, shift, return...
    return 4 * random.random() + 3
print("\nUniform distribution in the interval [3, 7)")
for i in range(10):
    print(my_random())

# Another way to generate random numbers from some interval
print(help(random.uniform))
print("\nUniform distribution in the interval [3, 7)")
for i in range(10):
    print(random.uniform(3,7))

# Not all random number generators are uniformily distributed
# For example, a normal distribution (aka "Bell Curve") may be required
print("\nNormal distribution with (Mean = 0) and (Standard Deviation = 1)")
for i in range(20):
    print(random.normalvariate(0,1))

print("\nNormal distribution with (Mean = 0) and (Standard Deviation = 9)")
for i in range(20):
    print(random.normalvariate(0,9))

print("\nNormal distribution with (Mean = 0) and (Standard Deviation = 0.2)")
for i in range(20):
    print(random.normalvariate(0,0.2))

print("\nNormal distribution with (Mean = 5) and (Standard Deviation = 0.2)")
for i in range(20):
    print(random.normalvariate(5,0.2))

# Or a discrete probability distribution may be required
print("\nDiscrete probability distribution in the interval (1, 6)")
for i in range(20):
    print(random.randint(1,6))

# Or a random element from a list may be required
outcomes = ['rock', 'paper', 'scissors']
print("\nA random element from a list: outcomes = ['rock', 'paper', 'scissors']")
for i in range(20):
    print(random.choice(outcomes))