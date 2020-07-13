# A standard data structure in computer science is an associative array (also called a map).
# In python it is called a dictionary (dictionaries are not ordered data).

# Friendface post
# user_id = 209
# message = "D5 E5 C5 C4 G4"
# language = "English"
# datetime = "20230215T124231Z"
# location = (44.590533, -104.715556)

post_01 = {"user_id":209,
           "message":"D5 E5 C5 C4 G4",
           "language":"English",
           "datetime":"20230215T124231Z",
           "location":(44.590533, -104.715556)}
# post_01 is a dictionary with 5 pieces of data
# if thought of as a map there are 5 inputs and 5 outputs
# in python inputs are called keys and outputs are called values

print(type(post_01))

post_02 = dict(message="SS Cotopaxi", language="English") # dictionary constructor
print(post_02)

post_02["user_id"] = 209
post_02["datetime"] = "19771116T093001Z"
print(post_02)

print(post_01['message']) # to access the value in the dictionary use single brackets around the key. An error will occur if the key does not exist.

# There are three solutions to prevent a KeyError
# Solution 1: if/else
if 'location' in post_02:
    print(post_02['location'])
else:
    print("The post does not contain a location value.")

# Solution 2: try
try:
    print(post_02['location'])
except KeyError:
    print("The post does not contain a location value.")

# Solution 3: get
print("\n", dir(post_02), "\n")
print(help(post_02.get))

location = post_02.get('location', None)
print(location)

# How to see all the data in a dictionary
print(post_01)
for key in post_01.keys():
    value = post_01[key]
    print(key, "=", value)

print("\n")
for key, value in post_01.items():
    print(key, "=", value)

print("\n", dir(post_01), "\n")