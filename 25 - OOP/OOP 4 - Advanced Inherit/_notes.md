# Advanced Inheritance

**Multiple inheritance** is when a class inherits from more than one parent class

- Child(Parent_A, Parent_B)

**Multilevel inheritance** is when a child inherits from a parent, which inherits from a grandparent

- Child(Parent) <- Parent(Grandparent) <- Grandparent

---

## Multiple Inheritance

```python
class Prey:
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator:
    def hunt(self):
        print(f"{self.name} is hunting")

class Fish(Prey, Predator):
    pass

fish = Fish("Nemo")


fish.flee()
fish.hunt()
```

- Here, fish has the attributes and methods of Prey and Predator

# Multilevel Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is eating")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Fish(Prey, Predator):
    pass

fish = Fish("Nemo")

fish.eat()
fish.sleep()

fish.flee()

fish.hunt()
```

- Here, all Prey and Predators have the attributes and methods of an Animal
- Fish inherits from Prey and Predator, so it is also an Animal

```
Fish  <-     Prey       <- Animal
        \- Predator <-/

```
