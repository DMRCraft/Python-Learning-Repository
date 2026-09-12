# User input can be done through the console for testing
# Use input(), which is a function that prompts the user to enter data

# Returns the entered data AS A STRING

name = input("What is your name? | ")
print(f"Hello, {name}!")

age = int(input("What age are you? | ")) # this *can* cause an error if a non-numerical value is given. Error handling is eventually used to fix this.

next_age = age + 1

print(f"You are {age} years old, and you will be {next_age} next year!")