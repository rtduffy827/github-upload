

user_input = input("Please enter a test string: ")

if len(user_input) < 6:
    print("Your string is too short.") # any size indentation works as long all the instructions line up

    print("Please enter a string with at least 6 characters.")
user_input = input("Please enter an integer: ")
number = int(user_input)

if ((number % 2) == 0):
    print("Your number is even.")
else:
    print("Your number is odd.")

# Scalene triangle: all sides have different lengths.
# Isosceles triangl: Two sides have the same length.
# Equilateral triangle: All sides are equal.

a = int(input("The length of side a = "))
b = int(input("The length of side b = "))
c = int(input("The length of side c = "))

if a != b and b != c and a != c:
    print("This is a scalene triangle.")
elif a == b and b == c: # elif = "else if"
    print("This is an equilateral triangle.")
else:
    print("This is an isosceles triangle.")