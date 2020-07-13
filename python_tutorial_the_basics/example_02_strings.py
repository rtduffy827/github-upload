# An example of a string using double quotes
message_01 = "Meet me tonight."
print(message_01)

# An example of a string using single quotes
message_02 = 'The clock strikes at midnight.'
print(message_02)

# Syntax error 1: using an apostrophe with single quotes
# message_03 = 'I'm looking for a someone to share in an adventure.'

# Syntax error 1: backslash solution (jargon = escapes the apostrophe)
message_03 = 'I\'m looing for someone to share in an adventure.'
print(message_03)

# Syntax error 1: double quotes solution
message_03 = "I'm looking for a someone to share in an adventure."
print(message_03)

# Syntax error 2: double quotes within double quotes (double quote inception)
# message_04 = "The phrase "Beam me up, Scotty" was never said on Star Trek."

# yntax error 2: single quote solution
message_04 = 'The phrase "Beam me up, Scorry" was never said on Star Trek.'
print(message_04)

# Use triple double quotes for a string that uses both double quotes and apostrophes
movie_quote = """One of my favorite lines from The Godfather is:
"I'm going to make him an offer he can't refuse."
Do you know who said this?"""
print(movie_quote)