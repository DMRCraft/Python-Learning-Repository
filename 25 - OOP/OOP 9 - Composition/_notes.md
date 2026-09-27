# Composition

Composition is OOP relationship where one object is made up of other objects, whose lifetimes are dependant on the containing object

An analogy is "You are a part of me, and your existence is tied to me"

```python
class Room:
    def __init__(self, name):
        self.name = name


class House:
    def __init__(self, *args):
        self.kitchen = Room("kitchen")
        self.bedroom = Room("bedroom")


house = House()

print(house.kitchen.name)
print(house.bedroom.name)
```

- The Rooms rely on the House object to exist. Note that Python doesn't enforce that a Room must be destroyed when the House is destroyed, since Composition isn't a special feature, but a design relationship
- You could also create a varying amount of rooms by using a list/dictionary -> `for room in house.rooms: print(...)`
