# Typecasting - the process of converting a variable from one data type to another.
#               str(), int(), float(), bool()

# Try testing different combinations of typecasting

name = "Dylan"
age = 15
grade = 80.5
is_student = True

print(type(is_student))


grade = int(grade) # truncates the decimal portion

age = float(age) # adds a decimal portion
age = str(age) # 15.0 -> "15.0" since above adds the .0
age += 1 # throws a TypeError - "can only concatenate str (not "int") to str"
age += "1" # string concatenation -> "15.0" + "1" = "15.01"

name = bool(name) # True if the name is NOT empty, else False if it is empty

bool("False")  # True
bool(0)        # False
bool(1)        # True
bool(-10)      # True

