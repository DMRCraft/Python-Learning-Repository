# *arg     - allows you to pass multiple non-key arguments
# **kwargs - allows you to pass multiple keyword-arguments (kwargs -> keyword arguments)
#          * unpacking operators


# ----- ARGS -----

def add(*args): # creates a tuple, the word "args" can be renamed also (try using: print(type(args)))
    total = 0
    for arg in args:
        total += arg
    return total

# print(add(1))
# print(add(1, 2, 3))
# print(add(1, 2, 3, 4, 5))

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

# display_name("Dylan")
# display_name("Dylan", "Ryan")
# display_name("Mr.", "Dylan", "Ryan")

# ----- KWARGS -----

def print_address(**kwargs): # creates a dictionary (try using: print(type(kwargs)))
    print(kwargs)
    for value in kwargs.values():
        print(value)

# print_address(street="123 Fake St.",
#                 city="Detroit",
#                 state="MI",
#                 zip="54321")


# You can combine args and kwargs

def shipping_label(*args, **kwargs): # args must be before kwargs
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs: print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else: print(f"{kwargs.get('street')}")
    
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Mr.", "Dylan", "Ryan",
               street="123 Fake St.",
               apt="#100",
               city="Detroit",
               state="MI",
               zip="54321")