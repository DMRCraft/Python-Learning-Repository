# zip() -> combines multiple iterables (lists, tuples, sets, dict etc) into a single iterator
#          Makes managing multiple indices easier!

# zip() creates a "zip object"

names = ["Dylan", "John", "Bob"]
ages = [15, 20, 25]
jobs = ["Student", "Manager", "Teacher"]

data = zip(names, ages, jobs)
# data = dict(zip(names, ages))

for name, age, job in data:
    print(f"{name} is {age} years old, and they're'a {job}")