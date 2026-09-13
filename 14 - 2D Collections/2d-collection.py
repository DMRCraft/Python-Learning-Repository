# 2D Collections - data structure that organizes elements into a grid format using rows and columns (matrix of data)
# access via two indices collection[0][1] - row=0, col=1

fruits = ["apple", "orange", "banana"]
vegetables = ["carrot", "broccoli", "potato"]
meats = ["ham", "chicken", "beef"]

groceries = [fruits, vegetables, meats]
# print(groceries)
# print(groceries[0]) # fruits list
# print(groceries[0][0]) # fruits list -> first item
# print(groceries[2][1]) # meats list -> second item

# you can also simply place an unnamed list into another list

# NOTE: YOU AREN'T JUST LIMITED TO LISTS, you can combine any structure types together
# E.g: [(), (), ...]
#      ({}, {}, ...)
#      {[], [], ...}

new_groceries = [
    ["apple", "orange", "banana"],
    ["carrot", "broccoli", "potato"],
    ["ham", "chicken", "beef"]
]

for collection in new_groceries:
    for food in collection:
        print(food, end=" ")
    print()