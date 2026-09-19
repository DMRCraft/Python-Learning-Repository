# An object is an instance of a class, or a "bundle" of
#       * related attributes (variables), and
#       * methods (functions)
#       E.g: A user can have attributes like name, age, id, etc
#            and methods like login, sign_out, etc

# A class is a blueprint used to design the structure and layout of an object

# . -> attribute access operator. Use to access attributes from objects

class Car:
    # self is kind of like "this" from JavaScript, except it isn't built-in. The __init__ method uses it
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


car1 = Car("Mustang", 2026, "red", False)
print(car1) # prints the object representation (memory address)
print(car1.model, car1.year, car1.color, car1.for_sale)

# See how we can create multiple objects from the same class
car2 = Car("Corvette", 2025, "blue", True)
print(car2.model, car2.year, car2.color, car2.for_sale)


print("----------")

from user import User

user1 = User("Dylan Ryan", 15, "123abc")
print(user1.name)
user1.hello()
user1.walk()
user1.speak("I am speaking, hi!")
