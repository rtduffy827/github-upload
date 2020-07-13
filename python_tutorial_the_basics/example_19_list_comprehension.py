# List: [1, 2, "a", 3.14]
# List Comprehensions:
# Basic forms - [expr for val in collection]
#               [expr for val in collection if <test>]
#               [expr for val in collection if <test> and <test2>]
#               [expr for val1 in collection1 and val2 in collection2]

# The original method
squares = []
for i in range(1, 101):
    squares.append(i**2)

print(squares)

# The List Comprehension method
squares_2 = [i**2 for i in range(1,101)]
print(squares_2)

remainders_5 = [x**2 % 5 for x in range(1,101)]
print(remainders_5)

remainders_11 = [x**2 % 11 for x in range (1,101)]
print(remainders_11)

# Quadratic Reciprocity:
# p_remainders = [x**2 %p for x in range (0, p)]
# len(p_remainders) = (p+1)/2
# First proved by Gauss

movies = ["Star Wars", "Gandhi", "Casablanca", "Shawshank Redemption", "Toy Story", "Gone with the Wind", "Citizen Kane", "It's a Wonderful Life", "The Wizard of Oz",
          "Gattaca", "Rear Window", "Ghostbusters", "To Kill A Mockingbird", "Good Will Hunting", "2001: A Space Odyssey", "Raiders of the Lost Ark", "Groundhog Day",
          "Close Encounters of the Third Kind"]

# Without List Comprehension
gmovies = []
for title in movies:
    if title.startswith("G"):
        gmovies.append(title)

print(gmovies)

# With List Comprehension
gmovies = [title for title in movies if title.startswith("G")]
print(gmovies)

# Sorting a list of movies by year
movies =[("Citizen Kane", 1941), ("Spirited Away", 2001), ("It's a Wonderful Life", 1946), ("Gattaca", 1997), ("No Country for Old Men", 2007), ("Rear Window", 1954),
         ("The Lord of the Rings: The Fellowship of the Ring", 2001), ("Groundhog Day", 1993), ("Close Encounters of the Third Kind", 1977), ("The Royal Tenenbaums", 2001),
         ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

pre2k = [title for (title, year) in movies if year < 2000]
print(pre2k)

# Vectors: scalar multiplication
v = [2, -3, 1]
print(4*v) # Incorrect answer: 4*v = v + v + v + v and Adding Lists = Concatenation
print([2, 4, 6] + [1, 3]) # another example of an unwanted outcome

w = [4*x for x in v]
print(w)

# Cartesian Product:
# If A and B are sets,
# then the Cartesian product
# is the set of pairs (a, b)
# where 'a' is in A and 'b' is in B.
# i.e. A x B = {(a, b) | a is a member of A, b is a member of B}
# Example,
# A = {1, 3}
# B = {x, y}
# A x B = {(1, x), (1, y), (3, x), (3, y)}

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)