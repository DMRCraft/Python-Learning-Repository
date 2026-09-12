# While loops - executes a block of code WHILE some condition remains true

import time

name = input("Enter your name | ")

while name == "":
    print("Please enter a name!")
    name = input("Enter your name | ")

print(f"Hello, {name}")

# ----------

food = input("Enter a food (q to quit) | ")

while not f"{food.lower()}" == "q":
    print(f"You like {food}")
    food = input("Enter a food (q to quit) | ")

print("Goodbye!")

# ----------

num = int(input("Enter a number between 1 and 10 | "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 and 10 | "))

print(f"You chose {num}")

# ----------
