# Nested Classes

A nested class is a class defined within another class. They are relatively uncommon, however, but are definitely useful to know

```
class Outer:
    class Inner:
```

- The inner class is grouped inside the outer class.
- It can be accessed through the outer class.
- Useful when the inner class is related to the outer class and isn't intended to be used independently.

## Benefits:

- Allows you to logically group classes that are closely related
- Encapsulates private details that aren't relevant outside of your outer class
- Keeps the namespace clear; reduces the possibility of naming conflicts

## Example:

```python
class House:

    class Room:
        def __init__(self, name):
            self.name = name

    def __init__(self):
        self.kitchen = self.Room("Kitchen")
        self.bedroom = self.Room("Bedroom")

house = House()

print(house.kitchen.name) # -> Kitchen
print(house.bedroom.name) # -> Bedroom

```
