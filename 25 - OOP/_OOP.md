# Object Oriented Programming

- I will be going back after OOP to properly polish these notes!

## Definitions:

- **Class** -> blueprint
- **Instance** -> (object) created from a class. Multiple can exist

---

- **Instance attribute** -> belongs to the instance
- **Class attribute** -> belongs to the class

## Creating a Class

```python
class Car:
    # self is given automatically, everything after are custom attributes
    def __init__(self, att1, att2, ...):
        self.att1 = att1
        self.att2 = att2

car1 = Car("attribute1", 2, 3.2, ...)
```

## Attribute Access Operator .

Use to access attributes and methods from objects

## Attribute

In the `__init__` method (constructor / initializer), you can create attributes
self.name = name / self.age = age / self.description = description

## Method

A method is written outside of the initializer. Access them with "."

- in an initializer, "self" must be written in the method, but Python automatically gives the properties of "self"

```python
class Car:
    def __init__(self, make):
        self.make = make

    # self is given to methods automatically, but you must declare it manually
    def drive(self):
        print(f"{self.make} is driving")

    def description(self, desc):
        print(f"{self.make} | {desc}")

car1 = Car("Mustang")
car1.drive()
car1.description("Cool car that drives")
```

## Class as a module

Simply create a separate file with the class, import in your main/other python file, and use the same method: <br>
car1 = Car(...)

## Some basic notes:

**vars(object)**

## Class attribute

variable defined directly in the class.
they are defined outside of the constructor
it is shared among all instances of that class (objects)
allows you to share data among all instances of the class

Good practice to access through the class instead of an instance

```python
class Student:
    class_year = 2024

    # pseudocode below, class_year is all that really matters here
    def __init__(self, ...)


Student.class_year # -> gets the class variable
```

---

## Inheritance

Allows a class to inherit attributes and methods from another class. They help with code reusability and extensibility
