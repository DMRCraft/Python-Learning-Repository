# Sorting can be accomplished with either .sort() or sorted()
# We can sort Lists, Tuples, Dictionaries, Objects, etc

# --- List ---

fruits = ["banana", "orange", "apple", "strawberry"]
fruits.sort() # Alphabetical order
print(fruits)

fruits.sort(reverse=True)
print(fruits)

nums = [1, 4, 2, 3]
nums.sort() # Numerical Order
print(nums)


# --- Tuple ---
fruits = ("banana", "orange", "apple", "strawberry")
fruits = tuple(sorted(fruits)) # CONVERTS IT TO A LIST! So we type-cast back to a tuple
# fruits = tuple(sorted(fruits, reverse=True))
print(fruits)


# --- Dictionary ---

fruits = {"banana": 105,
          "orange": 73,
          "apple": 72,
          "strawberry": 34}

# fruits = dict(sorted(fruits.items())) # TRUNCATES THE VALUES, and sorts the keys in alphabetical order by KEY, so we need to use .items()
                                      # and typecast to dict()

# fruits = dict(sorted(fruits.items(), key=lambda item: item[0], reverse=True)) # Full code example for reverse order. Compares KEYS

# ----------

fruits = dict(sorted(fruits.items(), key = lambda item: item[1])) # Sorts in order by VALUE
fruits = dict(sorted(fruits.items(), key = lambda item: item[1], reverse=True))

print(fruits)


# --- Dictionaries ---

class Fruit:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories}"

fruits = [Fruit("banana", 105),
          Fruit("orange", 73),
          Fruit("apple", 32),
          Fruit("strawberry", 34)]

#                                  object
fruits = sorted(fruits, key=lambda fruit: fruit.name)
# fruits = sorted(fruits, key=lambda fruit: fruit.name, reverse=True)

# fruits = sorted(fruits, key=lambda fruit: fruit.calories)
fruits = sorted(fruits, key=lambda fruit: fruit.calories, reverse=True)

print(fruits)