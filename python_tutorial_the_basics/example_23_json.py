# JSON = Java Script Object Notation
# It is a small lightweight data format.
# A packet of JSON data is almost identical to a python dictionary.
# It is shorter than XML (Extensible Markup Language) and
# it can be quickly be parsed by browsers since it uses JavaScript syntax.
# This makes JSON an ideal format for transfering data between a client and a server.
# If the client is not a browser do not worry, Android and other mobile operating systems
# all come equipped with tools for parsing and working with json.

# A typical JSON data packet:
# {
#     "title" : "Gattaca",
#     "release_year" : 1997,
#     "is_awesome" : true,
#     "won_oscar" : false,
#     "actors" : ["Ethan Hawke", "Uma Thurman", "Alan Arkin",
#                 "Loren Dean"],
#     "budget" : null,
#     "credits" : {
#         "director" : "Andrew Niccol",
#         "writer" : "Andrew Niccol",
#         "composer" : "Michael Nyman",
#         "cinematographer" : "Sławomir Idziak"
#     }
# }

# Notice the above looks just like a python dictionary with a few exceptions.
# True and false are not capitalized in JSON, but in python they are.
# Instead of None the JavaScript value null is used.
# This JSON object contains examples of all possible data types: 
# # string, numbers, booleans, a list, null, or even another JSON object.

# Equivalent code in XML:
# <movie>
#   <title>Gattaca</title>
#   <release_year>1997</release_year>
#   <is_awesome>1</is_awesome>
#   <won_oscar>0</won_oscar>
#   <actors>
#     <actor>Ethan Hawke</actor>
#     <actor>Uma Thurman</actor>
#     <actor>Jude Law</actor>
#     <actor>Lorean Dean</actor>
#   </actors>
#   <budget/>
#   <credits>
#     <director>Andrew Niccol</director>
#     <writer>Andrew Niccol</writer>
#     <composer>Michael Nyman</composer>
#     <cinematographer>Sławomir Idziak</cinematographer>
#   </credits>
# </movie>

# The increased size of XML data is largerly due to the end tags
# repeating the text of the opening tags.

# Recommendation: Learn the pros and cons of each format 
# then choose the one best situated for a particular project.

# ===== How to use the JSON Module in python =====
# Save the example JSON data packe as 'movie_1.txt', with UTF-8 encoding.
import json

# Key Methods -
# json.load(f): Load JSON data from file (or file-like object).
# json.loads(s): Load JSON data from a string.
# json.dump(j, f): Write JSON object to file (or file-like object).
# json.dumps(j): Output JSON object as string.
print(dir(json), "\n")

# <json.load> example:
json_file = open("movie_1.txt", "r", encoding="utf-8")
movie = json.load(json_file)
json_file.close()

# Unicode character 142 = ł
print(movie, "\n")
print(type(movie))
print(movie["title"])
print(movie["actors"])
print(movie["release_year"])

# <json.loads> example:
# Use this function if data arrives in the form of a string.
# This is common in client/server applications where data is sent over the internet.
value = """{"title": "Tron Legacy",
            "composer": "Daft Punk",
            "release_year": 2010,
            "budget": 170000000,
            "actors": null,
            "won_oscar": false
            }"""
tron = json.loads(value)
print("\n",tron)

# <json.dumps> example:
# Suppose the data about Gattaca needs to be stored in a database or sent to a remote user.
# To do this convert the 'movie' dictionary into a valid JSON string.
print(json.dumps(movie, ensure_ascii=False))

# <json.dump> example:
# Create a new object, convert it to JSON, and then write it to a file.
movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["composer"] = "John Williams"
movie2["actors"] = ["Tome Cruise", "Colin Farrell",
                    "Samanta Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski" # ń |0x144| latin small letter n with acute.

file = open("movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file, ensure_ascii=False)
file.close()

# Open movie_2.txt to see that everything is saved and formatted correctly.