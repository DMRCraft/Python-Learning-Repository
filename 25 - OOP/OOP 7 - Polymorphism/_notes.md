# Polymorphism

Polymorphism allows different types of objects to use the same method or interface, while each object can behave differently.  
Polymorphism is a greek word (poly = many, morphe = form)

There are two different ways to achieve polymorphism:

1. Inheritance Polymorphism -> an object can be treated of the same type as a parent class
2. Duck-Typing -> the object must have necessary attributes/methods

Python doesn't care about what class the object is. It only cares about what methods it has

## Inheritance Polymorphism:

```python
from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

# ----------

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

# We can create objects directly in a collection!
shapes = [Circle(5), Pizza("cheese", 10)]
for shape in shapes:
    shape.area()
```

In this example:

- Shape defines a common "area()" method
- Circle provides its own implementaion of it
- Pizza inherits from Circle, so it also inherits its "area()" method
- In the loop, it doesn't care about whether it is a shape, but whether it has the appropiate methods

You can also do this below, since Pizza is also a Shape! [Pizza <-- Circle <-- Shape]

```python
# ...
class Pizza(Circle):
    def area(self):
        print("Calculating pizza area...")
        return 3.14 * self.radius ** 2
```

## Duck-Typing

The common analogy is: _"If it walks like a duck and quacks like a duck, treat it like a duck"_

```python
class Animal:
    alive = True

# ---

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = True
    def speak(self):
        print("BEEP!")

cat = Cat()
cat.alive = False

# We can create object directly inside of a collection! We can also add our own named objects too.
animals = [Dog(), cat, Car()]
for animal in animals:
    animal.speak()
    print(animal.alive)

```

In the example:

- Car is not an Animal, but it can be treated as one since it holds the minimun necessary attributes and methods to be an Animal
- Not related to Polymorphism, but remember you can change class attributes
