# List comprehension - a concise way to create lists in Python. They are compact and easier to read, rather than traditional loops
#                      [expression for value in iterable if condition]
#                                                        if condition is optional


# Here is an example with an ordinary loop

doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)

doubles.clear()

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]
print(squares)


# --- Strings ---

fruits = ["apple", "orange", "banana"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits] # return the first character of each string
print(fruit_chars)

# --- Conditions ---

numbers = [1, -2, 3, -4, 5, -6, -7, 8]

#               return num
positive_nums = [num for num in numbers if num >= 0] # return num if it is >= 0 (positive)
full_positive_nums = [abs(num) for num in numbers]

even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(even_nums, odd_nums, sep=" - ")

# ---

grades = [85, 42, 21, 95, 40, 39]

passing_grades = [grade for grade in grades if grade >= 40]
failing_grades = [grade for grade in grades if grade < 40]
print(passing_grades)
