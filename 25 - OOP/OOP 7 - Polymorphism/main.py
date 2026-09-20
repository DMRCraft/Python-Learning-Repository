# Polymorphism -> refers to methods/functions/operators with the same name that can be executed on many objects or classes
# Polymorphism is a greek word (poly = many, morphe = form)

# Two wats to achieve polymorphism:
#   1. Inheritance -> an obkect can be treated of the same type as a parent class
#   2. "Duck typing" -> object must have necessary attributes/methods

# Python doesn't care about what class the object is. It only cares about what methods it has

from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Triange(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping



# Pizza has three forms, Pizza, Circle and Shape

shapes = [Circle(4), Square(5), Triange(6, 7), Pizza("cheese", 10)]

for shape in shapes:
    print(shape.area())

