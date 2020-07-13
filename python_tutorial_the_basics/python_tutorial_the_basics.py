# Python code to demonstrate 
# to find strings with substrings 
# using list comprehension 

# initializing list 
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms'] 

# printing original list 
print ("The original list is : " + str(test_list)) 

# initializing substring 
subs = 'Geek'

# using list comprehension 
# to get string with substring 
res = [i for i in test_list if subs in i] 

# printing result 
print ("All strings with given substring are : " + str(res)) 

# Python code to demonstrate 
# to find strings with substrings 
# using filter() + lambda 

# initializing list 
test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms'] 

# printing original list 
print ("The original list is : " + str(test_list)) 

# initializing substring 
subs = 'Geek'

# using filter() + lambda 
# to get string with substring 
res = list(filter(lambda x: subs in x, test_list)) 

# printing result 
print ("All strings with given substring are : " + str(res)) 

pattern_string = "string"
pattern_list = [2, 3, 5, 7, 11, 13,17]
pattern_tuple = (1, 4,9, 16, 25, 36)

number_of_elements = len(pattern_string)
print(pattern_string[0:number_of_elements])
print(pattern_list[0:-1])
print(pattern_tuple[0:-1])

value = ''
print(value)
for element in pattern_tuple:
    value += str(element)

print(value)