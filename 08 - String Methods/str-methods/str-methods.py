# String Methods - built-in functions and methods used to manipulate strings
# NOTE: Python uses zero-based numbering

# Use these function to get a list of all string methods available, and what they do
print(dir(str))
print(help(str)) # press space to go through the different pages


name = input("Enter a name | ")


length = len(name) # returns the length of the string, including spaces

result = name.find(" ") # finds the FIRST occurance of the given value and returns the INDEX. If no value found, returns -1 instead
result = name.rfind("r") # finds the LAST occurance of the given value and returns the INDEX. If no value found, returns -1 instead

name = name.capitalize() # capitalizes the first letter in a string, returns a STRING
name = name.upper() # capitalizes ALL characters in a string, returns a STRING

result = name.isdigit() # returns a boolean, True if the string only contains numerical values
result = name.isalpha() # returns a boolean, True if the string only contains ALPHABETIC values. Spaces are NOT alphabetical values

# --------------------------------------------

phone_number = input("Enter a phone number | ")

result = phone_number.count("-") # counts the amount of times the value occurs in a string, and returns an integer

phone_number = phone_number.replace("-", " ") # replaces all occurances of the first value with the second value, returns a new string
phone_number = phone_number.replace("-", "") # -> could be used in a phone number validation program
