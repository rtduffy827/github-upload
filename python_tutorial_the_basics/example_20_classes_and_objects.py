# It is recommended that class names are capitalized

import datetime

class Users: # This class does nothing but pass
    pass

user_1 = Users() # user_1 is an instance of the class User()
# Data attached to an object is called a field
user_1.first_name = "Dave"
user_1.last_name = "Bowman"

# Style Guide for Python (PEP 8)
# Naming Fields: "...lowercase with words seperated by underscores as necessary to improve readability."
print(user_1.first_name)
print(user_1.last_name)

first_name = "Arthur"
last_name = "Clarke"

print(first_name, last_name)
print(user_1.first_name, user_1.last_name)

user_2 = Users()
user_2.first_name = "Frank"
user_2.last_name = "Poole"

print(first_name, last_name)
print(user_1.first_name, user_1.last_name)
print(user_2.first_name, user_2.last_name)

user_1.age = 37
user_2.favorite_book = "2001: A Space Odyssey"

print(user_1.age)
# print(user_2.age) # Returns an error

# Class Features:
# - Methods
# - Initialization
# - Help text

class User:
    """A member of FriendFace. For now we are
    only storing their name and birthday.
    But soon we will store an uncomfortable
    amount of user information."""
    def __init__(self, full_name, birthday):  # first thing to add is an init method (a.k.a Constructor)
        self.name = full_name
        self.birthday = birthday # yyyymmdd
        # Extract first and last names
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]
    def age(self):
       """Return the age of the user in years."""
       today = datetime.date(2001, 5, 12)
       yyyy = int(self.birthday[0:4])
       mm = int(self.birthday[4:6])
       dd = int(self.birthday[6:8])
       dob = datetime.date(yyyy, mm, dd) # Date of birth
       age_in_days = (today - dob).days
       age_in_years = age_in_days / 365
       return int(age_in_years)

user = User("Dave Bowman", "19710315")
print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)

print(help(User))

print(user.age())