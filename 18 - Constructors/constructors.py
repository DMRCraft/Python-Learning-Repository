# Constructors - special method used to create a new object, often while optionally giving it some additional data

# Use constructors like list(), set(), etc
#    when you want to create a collection from another iterable or value,
#    especially for type conversion.
#    Use [], (), etc. when directly creating the collection with known values.

# some examples:
# list()
# set()
# tuple()
# dict()
# str()
# int()
# float()

numbers = [1, 2, 3]
num_set = set(numbers)
print(num_set)

# ---
my_range = range(10)
print(my_range)

# ---

# you can create empty collections
my_list = list() # -> []