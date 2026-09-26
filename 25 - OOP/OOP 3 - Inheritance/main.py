# Inheritance - allows a class to inherit attributes and methods from another class

# class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

# Despite not including anything from the Animal class, it inherits them. We do not need to rewrite the code for each child
class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Lucky")
cat = Cat("Sir Meows alot")
mouse = Mouse("Jerry")

print(dog.name)
print(cat.is_alive)
mouse.eat()

Animal.sleep()