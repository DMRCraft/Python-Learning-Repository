# Collection (data structure) is a data type used to store and organise multiple values as a single object / "variable"

# List []  | ordered, mutable, changeable collection, and duplicates are OK
# Set {}   | unordered and mutable adding and removing are fine. NO duplicates
# Tuple () | ordered and unchangeable. Duplicates are OK

# For a list of methods available to a certain collection, use:
# print(dir(collection)) - alphabetical list of methods
# print(help(collection)) - documentation for the object


# TO DO LATER - seperate all collections into different .py files

fruits = ["apple", "orange", "banana", "strawberry"]

print(fruits[0])
print(fruits[0:3]) # these work as string indexing
print(fruits[::2])

# for item in collection
for fruit in fruits:
    print(fruit)

print(len(fruits))
print("apple" in fruits) # the "in" operator returns a boolean, True if the collection contains it, else False

# ----- LISTS -----

fruits[1] = "pineapple"

fruits.append("coconut")    # append to the end of the list
fruits.remove("apple")      # remove the first occurance of "apple"
fruits.insert(0, "grape")   # insert "grape" at index 0
fruits.sort()               # sort into ALPHABETICAL ORDEWR
fruits.reverse()            # reverse the list

print(fruits.index("apple"))  # returns the index of the first occurance. Throws a ValueError if isn't found
print(fruits.count("coconut"))

fruits.clear()              # remove all elements

print(fruits)

# -------------------------

# ----- SETS -----

vegetables = {"broccoli", "carrot", "potato"}
print(vegetables) # restart the program multiple times and see the order change

print(len(vegetables))
print("brocoli" in vegetables)

vegetables.add("lettuce")
vegetables.pop() # removes an arbitrary element
vegetables.clear()

print(vegetables)

# -------------------------

# ----- Tuples -----

colors = ("red", "orange", "yellow")
print(len(colors))
print("red" in colors)
print(colors.count("red"))