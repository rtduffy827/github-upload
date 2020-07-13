# There are wo types of files generally.
# Text Files:       |   Binary Files:
# - Plain Text      |   - Compiled code
# - XML             |   - App data
# - JSON            |   - Media files
# - Source Code     |         ~ images
# ⋮                 |         ~ audio
#                   |         ~ video
#                   |   ⋮

# The focus will be on the file and the mode arguments of the built-in open function.
# print(help(open))

# ===== Opening and reading a file =====
# The basic method for dealing with files.
f = open("txt_files/guido_bio.txt") # Default mode is read-only.
text = f.read()
f.close()

print(text)

# The danger with the above method is if something goes wrong before the file is closed.
# This could lead to memory leaks on the system with a number of unclosed files.
# The solution is the 'with' keyword. It is both safer and slightly shorter.
# This keyword will take care of opening and closing the file even if an exception is throun.
with open("txt_files/guido_bio.txt") as fobj:
    bio = fobj.read()
print(bio)

# When file does not exist then Python throws an exception called FileNotFoundError.
# The below code accounts for this possibility.
try:
    with open("future_lottery_number.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)

try:
    with open("txt_files/guido_bio.txt") as f:
        text = f.read()
except FileNotFoundError:
    text = None

print(text)

# ===== Writing to a file =====
oceans = ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"]

with open("txt_files/oceans.txt", "w") as f:
    for ocean in oceans:
#        f.write(ocean) # Writes each item of the list to the text file (will not assume separators are wanted).
#        f.write("\n") # Puts a newline separator after each item in the list.
         print(ocean, file=f) # Combines the two methods above.

# ===== Appending to a file =====
# A means of writing to a file without overwriting it.
with open("txt_files/oceans.txt", "a") as f:
    print(23*"=", file=f)
    print ("These are the 5 oceans.", file=f)