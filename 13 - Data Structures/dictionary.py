# Dictionary - collection of {key : value} pairs
#              ordered and changeable, but no duplicates

capitals = {"USA": "Washington D.C",
            "India": "New Delhi",
            "Ireland": "Dublin",
            "France": "Paris"}


print(capitals.get("USA")) # .get(key) -> either returns the value of that key or "None" if the key doesnt exist
if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"}) # inserts a new key:value pair into the dictionary
capitals.update({"Ireland": "Cork"}) # updates an existing key, just use the same key name with a new value

capitals.pop("India") # removes the key:value pair from the dictionary
capitals.popitem() # removes the latest key:value pair
capitals.clear() # clears the dictionary

keys = capitals.keys() # returns an object of all keys in a dictionary (doesn't return the values)
print(keys)

for key in capitals.keys(): 
   print(key + ": " + capitals.get(key))

values = capitals.values() # returns an object of all values in a dictionary (doesn't return the keys)
print(values)

for value in capitals.values:
    print(value)

items = capitals.items() # returns a dictionary object that resembles a 2D collection of list + tuples [(), (), ()]
for key, value in capitals.items():
    print(f"{key}: {value}")