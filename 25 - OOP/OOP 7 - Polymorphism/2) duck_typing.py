# "Duck typing" is another way to achieve polymorphism.
#               The object must have the minimum necessary attributes & methods

# The common analogy is: "If it walks like a duck and quacks like a duck, treat it like a duck"


# In this example, Car is not an animal, but can still be treated like one since it has a "speak" method and an "alive" attribute

class Animal:
    alive = True

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

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)