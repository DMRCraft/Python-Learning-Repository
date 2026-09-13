# Function - holds a piece of code that runs a specific task, which can be reused
#            they can take in arguments (pieces of data) and return a value to the caller

# Return - statement used to end a function, and (optionally) send back a result value

# PARAMETER - the name inside of the function
# ARGUMENT - the data which the caller passes

# Types of arguments:
# 1. positional | 2. default | 3. keyword | 4. arbitrary

def happy_birthday():
    print("Happy birthday to you,")
    print("Happy birthday to you!")
    print("Happy birthday to 'user',")
    print("Happy birthday to you!")

# happy_birthday()

def greet_user(user, age ): # these are parameters
    print(f"Hello, {user}, you are {age} years old")

# matching arguments 
greet_user("Dylan", 15) # these are arguments



def add(x, y):
    return x + y

z = add(2, 3) # assign a function to a variable
print(z)
print(add(9, 7)) # or directly use the return value
