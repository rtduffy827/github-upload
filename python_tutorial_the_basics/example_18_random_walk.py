# The Plan: Write random walk function
# Version 1) Simple
# Version 2) Short
import random

def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        elif step == 'W':
            x = x - 1
        else:
            print("Error: <step = random.choice(['N', 'S', 'E', 'W'])> did not produce one of the 4 choices")
    return (x, y)

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home =",
          abs(walk[0]) + abs(walk[1]))

def random_walk_2(n):
    """Return coordinates after 'n' block random walk."""
    x , y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

for i in range(25):
    walk = random_walk_2(10)
    print(walk, "Distance from home =",
          abs(walk[0]) + abs(walk[1]))

number_of_walks = 20000

for walk_length in range(1, 31):
    no_transport = 0 # Number of walks 4 or fewer blocks from home
    for i in range(number_of_walks):
        (x, y) = random_walk_2(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            no_transport += 1
    no_transport_percentage = float(no_transport) / number_of_walks
    print("Walk size =", walk_length,
          "/ % of no transport =", 100*no_transport_percentage)