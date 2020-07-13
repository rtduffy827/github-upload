# Boolean values: True, False

# Note True and False both must start with a capital letter
print("There are only two boolean values", True, "and", False, "\n")

a = 3
b = 5
print("a =", a)
print("b =", b)
print("(a = b) is", a == b)
print("(a != b) is", a != b) # ! is used as the logical 'not' in many programing languages
print("(a > b) is", a > b)
print("(a < b) is", a < b)

print("\nTrue is of type", type(True))
print("False is of type", type(False))

# Boolean Conversions
# trivial -> False
# non-trivial -> True
print("\nbool(28) =", bool(28))
print("bool(-2.71828) =", bool(-2.71828))
print("bool(0) =", bool(0))

print("""\nbool("Turing") =""", bool("Turning"))
print("""bool(" ") =""", bool(" "))
print("""bool("") =""", bool(""))

print("\nstr(True) =", str(True))
print("str(False) =", str(False))
print("int(True) =", int(True))
print("int(False) =", int(False))
print("5 + True =", 5 + True) # 1 <--> True
print("10 * False =", 10 * False) # 0 <--> False