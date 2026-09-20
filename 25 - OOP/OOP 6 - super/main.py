# super() is a function used in a child class to call methods from a parent class (superclass)
#         allows you to extend the functionality of the inherited method(s)

# In the child's constructor:
#   super().__init__(arguments) -> we are calling the parents initializer
#   super().method() -> calls "method" from the parent


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        print(f"Is is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"Is is a square with an area of {self.width * self.width}cm^2")
        super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"Is is a triangle with an area of {self.width * self.height / 2}cm^2")
        


circle = Circle("red", True, 10)
square = Square(color="blue", is_filled=False, width=5)     # You *can* add keyword arguments if you want to, not required
triangle = Triangle(color="yellow", is_filled=True, width=5, height=10)

print(vars(circle))
print(vars(square))
print(vars(triangle))

print()

circle.describe()
print()
square.describe()
print()
triangle.describe()

