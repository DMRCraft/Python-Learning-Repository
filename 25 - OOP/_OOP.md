# Object Oriented Programming

## Creating a Class

```python
class Car:
    # self is given automatically, everything after are custom attributes
    def __init__(self, att1, att2, ...):
        self.att1 = att1
        self.att2 = att2

car1 = Car("attribute1", 2, 3.2, ...)
```

**Attribute Access Modifier .** -> Use to access attributes from objects

## Attribute

In the `__init__` method, you can create attributes
self.name = name / self.age = age / self.description = description

## Method

A method is written outside of the `__init__` method. Access them with "."

```python
class Car:
    def __init__(self, make):
        self.make = make

    # self is given to methods automatically
    def drive(self):
        print(f"{self.make} is driving")

    def description(self, desc):
        print(f"{self.make} | {desc}")

car1 = Car("Mustang")
car1.drive()
car1.description("Cool car that drives")
```

## Class as a module

Simply create a seperate file with the class, import in your main/other python file, and user the same method: <br>
car1 = Car(...)

## Some basic notes:

**vars(object)**
