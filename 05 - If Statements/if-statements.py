# if statements - control-flow structure that exectures a block of code if a Boolean expression is True.

age = int(input("Enter your age | "))

if age >= 18:
    print("You are an adult")
elif age < 0:
    print("You are not a valid age")
else:
    print("You are a minor")

# NOTE: you can use the variable name to check a True/False statement

# if age has a value, run the first block, else run the second block
if age:
    ...
else:
    ...