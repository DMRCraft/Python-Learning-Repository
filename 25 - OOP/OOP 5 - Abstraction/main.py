# Abstraction is an OOP principle that hides unnecessary implementation details and only exposes the essential functionality
# Abstract class -> a class that cannot be instantiated on its own / meant to be subclasses

#       They can contain abstract methods, which are declared but have no implementation

# Benefits of abstraction: Prevents instantiation of the class itself and requires children to inherit abstract methods


# abc - abstract base class
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod # decorator, learned later
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# vehicle = Vehicle() # -> This causes a TypeError -> you cannot create an instance of an abstract class!

# You MUST implement all abstract methods
# class Car(Vehicle):
#     pass

# car = Car() 

class Car(Vehicle):
    def go(self):
        print("The car is driving")

    def stop(self):
        print("Stopping the car!")

class Motorcycle(Vehicle):
    def go(self):
        print("The motorcycle is driving")

    def stop(self):
        print("Stopping the motorcycle!")

car = Car()
car.go()
car.stop()

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()