# Inheritance

Inheritance is an OOP concept that allows a class to inherit attributes and methods from another class, while also allowing it to add or override functionality. <br>

- The parent class is called the **"superclass"** <br>
- The child class is called the **"subclass"**

To inherit from a superclass, use:  
`Child(Parent):  
    ...`

Inheritance represents an **"is-a"** relationship

## Examples

### 1) Basic Syntax

```python
class Animal:
    def speak(self)
        print("The animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        self.name = name

dog = Dog("Max")

dog.speak()
print(dog.name)

```

### 2) Shared attributes

```python
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog("Lucky")
cat = Cat("Sir Meows alot")

print(dog.name)
print(cat.is_alive)
dog.eat()
cat.sleep()
```

### 3) Method Overriding

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Lucky")
cat = Cat("Sir Meows alot")

dog.speak()
cat.speak()

```

---

## super()

Look at OOP 6, is a function used in a child class to call methods from a parent class (superclass)
