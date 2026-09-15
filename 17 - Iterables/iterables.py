# Iterables - object/collection that can return its elements one at a time,
#             allowing it to be iterated over in a loop

# NOTE: Below, a list is used. You can replace the list to be a tuple, set, etc. They are all iterable

numbers = [1, 2, 3, 4, 5]

# Good practice to name the iteration variable based on the items being iterated over.
for num in numbers:
    print(num)

print("-----")

for num in reversed(numbers):
    print(num)

print("-----")

# NOTE: Sets are NOT REVERSABLE
fruits = {"apple", "orange", "banana", "coconut"}
for fruit in fruits:
    print(fruit)

print("-----")

name = "DMR Craft"

for character in name:
    print(character, end=" ")

print("-----")

my_dictionary = {"A": 1, "B": 2, "C": 3}
# simply iterating over a dictionary returns all keys
for item in my_dictionary:
    print(item)

print("-----")

# return all of the values
for item in my_dictionary.values():
    print(item)

print("-----")

# return both key: value
for key, value in my_dictionary.items():
    print(f"{key}: {value}")
