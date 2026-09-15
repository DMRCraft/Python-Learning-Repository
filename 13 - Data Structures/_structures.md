# Collections

## List `[]`

An ordered, mutable collection that allows duplicate values.

**Common methods:**

```python
list.append(x)       # Add to end
list.extend(iterable) # Add multiple values
list.insert(i, x)    # Insert at index
list.remove(x)       # Remove first occurrence
list.pop(i)          # Remove and return item
list.clear()         # Remove all items
list.index(x)        # Find index
list.count(x)        # Count occurrences
list.sort()          # Sort in place
list.reverse()       # Reverse in place
list.copy()          # Create a shallow copy
```

---

## Set `{}`

An unordered, mutable collection containing unique values.

**Common methods:**

```python
set.add(x)           # Add an item
set.remove(x)        # Remove an item; raises KeyError if absent
set.discard(x)       # Remove an item; does nothing if absent
set.pop()            # Remove and return an arbitrary item
set.clear()          # Remove all items
set.copy()           # Create a shallow copy

set.update(iterable) # Add multiple items
set.union(other)     # Combine sets
set.intersection(other) # Common items
set.difference(other)   # Items only in this set
set.symmetric_difference(other) # Items in either, but not both

# IMPORTANT NOTE: {} is NOT an empty set, it is an empty dictionary
```

---

## Tuple `()`

An ordered, immutable collection that allows duplicate values.

**Common methods:**

```python
tuple.count(x)       # Count occurrences
tuple.index(x)       # Find index
```

---

## Dictionary `{key: value}`

A mutable collection of key-value pairs where each key is unique.

**Common methods:**

```python
dict.get(key)        # Get value; returns None if key is absent. NOTE: None is NOT A STRING, it is a value
dict.keys()          # Return keys
dict.values()        # Return values
dict.items()         # Return key-value pairs as [(), (), ..]
dict.update(key, value)   # Add/update key-value pairs
dict.pop(key)        # Remove and return value
dict.popitem()       # Remove and return last key-value pair
dict.clear()         # Remove all items
dict.copy()          # Create a shallow copy
dict.setdefault(key, default) # Get value or insert default
```

---

## Quick comparison

| Collection | Ordered | Mutable | Duplicates | Main purpose         |
| ---------- | ------- | ------- | ---------- | -------------------- |
| List       | Yes     | Yes     | Yes        | General ordered data |
| Tuple      | Yes     | No      | Yes        | Fixed data           |
| Set        | No      | Yes     | No         | Unique values        |
| Dictionary | Yes\*   | Yes     | Keys: No   | Key-value data       |

---

## What is the point of tuples, if you can't change or add to them?

Simply, they are used for a grouped set of values that are guarenteed to not be changed <br>
E.g: cords = (10, 20) <br>
Another example: location = {
(10, 20): "Home",
(100, -20): "Village"
}

## enumerate()

Use for cases like this:

```python
foods = ["apple", "carrot", "pizza"]

for iteration_num, food in enumerate(foods, start=1):
    print(f"{iteration_num}: {food}")

# output: 1: apple  2: carrot  3: pizza

```

- enumerate turns: foods = ["apple", "carrot", "pizza"]
- into pairs: (0, "apple") (1, "banana") (2, "pizza")
