
class User:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

    def hello(self):
        print(f"Hello! I am {self.name}")

    def walk(self):
        print(f"{self.name} is walking")

    def speak(self, message):
        print(f"*{self.name}*: {message}")