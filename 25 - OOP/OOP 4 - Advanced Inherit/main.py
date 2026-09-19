# Multiple inheritance - inherit from more than one parent class | C(A, B)

# Multilevel inheritance - inherit from a parent, which inherits from a grandparent
#                          C(B) <- B(A) <- A


# Here, the system is:  Animal ->    Prey   -> Rabbit + Fish
#                            \ -> Predator -> Hawk  +  Fish

#      <- Animal - >
#    ↓              ↓
#   Prey        Predator
#   ↓               ↓
#  Rabbit > Fish < Hawk

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

# Rabbits are prey, so they can flee
class Rabbit(Prey):
    pass

# Hawks are predators, so they can hunt
class Hawk(Predator):
    pass

# Fish can hunt, but also flee from bigger fish
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

rabbit.flee()
rabbit.eat()

hawk.hunt()
hawk.sleep()

fish.hunt()
fish.flee()
fish.eat()


