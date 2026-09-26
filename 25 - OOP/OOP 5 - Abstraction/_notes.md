# Abstraction

Abstraction is an OOP principle that hides unnecessary implementation details and only exposes the essential functionality  
An abstract class is a class that cannot be instantiated on its own / meant to be subclassed. They can contain abstract methods, which are declared but have no implementation

### Import the following to use!

```python
from abc import ABC, abstractmethod
```

## Benefits of abstraction:

- Prevents instantiation of the class itself
- Requires children to inherit abstract methods

## Example

```python
from abc import ABC, abstractmethod

# Inherit fron the ABC class
class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

# ---------------------

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

```

In this example, Car and Motorcycle inherit from the abstract class. Both have different implementations of the abstract methods.

If you do not include a method, it will cause an error.

You also cannot create a Vehicle instance, it will cause a TypeError. This is great for when you do not want instances of a certain class (For example, don't allow Animal instances, but a Cat or Dog are allowed)
