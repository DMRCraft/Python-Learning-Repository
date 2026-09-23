# Object Oriented Programming Introduction

## What is OOP?

**Object Oriented Programming (OOP)** is a programming technique that organises code around objects, which can contain:

- **Attributes** -> data / state / variables
- **Methods** -> behaviour / functions

---

### Class

A class is a blueprint used to design the structure and layout of an object

### Object

An object is an instance of a class, stored in memory. It is a particular thing/value created from a class

### Instance

An instance is basically a synonym for an object, but it is an object considered in relation to its class
(for example, a dog object is **an instance** of the Dog object)

```
Player         (class)
    -> player1 (object / instance)
    -> player2 (object / instance)

```

## Class Syntax:

```python

class Player:
    # ...

player1 = Player(...)
player2 = Player(...)

```

---

## Initializing

`__init__` is a special method that is automatically called when an object is created.

It is commonly used to initialise an object's attributes, or to run basic logic.
"self" is an argument given by `__init__`. It refers to the particular instance that the method is running on

```python
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

player1 = Player("Dylan", 100)
player2 = Player("John", 54)

```

---

## Attribute Access Operator -> .

Use "." to access attributes and methods of an object

## Instance attribute

An instance attribute is data belonging to a particular object, mainly created using self/initialisation
E.g: creating two objects, Player("Dylan") and Player("John"), both have their own values

```python
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

player = Player("Dylan", 100)

player.name
player.health

```

## Method

A method is a function defined inside a class.
Each method is also given "self" as its first parameter, referring to the object the method is running inside of.

```python

class Player:
    def greet(self):
        print("Hello!")

player = Player(...)

player.greet()

```

---

# Complete Example

```python
class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def greet(self):
        return f"Hi, I am {self.name}!" # you can return values like normal functions

    def change_health(self, amount):
        self.health += amount

player1 = Player("Dylan", 100)
player2 = Player("John", 54)

print(player1.greet())

player2.change_health(-10)
player2.change_health(20)
print(player2.health)
```
