# Aggregation - "has-a" relationship

# Composition is OOP relationship where one object is made up of other objects,
#             whose lifetimes are dependant on the containing object
#             "You are a part of me, and your existance is tied to me"

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)] # creates 4 wheels

    def display_car(self):
        return f"{self.make} {self.model} {self.engine.horse_power}(hp) {self.wheels[0].size}in"


car1 = Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)
car2 = Car(make="Chevrolet", model="CorvetteMustang", horse_power=700, wheel_size=20)

print(car1.display_car())
print(car2.display_car())

