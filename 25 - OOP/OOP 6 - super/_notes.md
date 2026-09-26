# super()

**super()** is a function used in a child class to call methods from a parent class (superclass)
It allows you to extend the functionality of the inherited method(s)  
Think of **_self_** as the object, and **_super_** as the parent

In the child's constructor:

- `super().__init__(arguments)` -> we are calling the parents initializer
- `super().method()` -> calls "method" from the parent

By creating a child `__init__`, you replace the parent's initializer. So, you can call the parent initializer seperately with `super().__init(arguments)`

## Why use?

When a child defines its own `__init__`, the parent's `__init__` is not automatically called. If the child wants the parent's initialization to happen, it must explicitly call it with super()

```python
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

circle = Circle(10)
# We cannot send a "color" argument.
```

## Example

```python
class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {"filled" if self.is_filled else "not filled"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        # Call the parent's initializer, then initialize my own attributes
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        # Do logic, then call the parent's describe method
        print(f"Is is a circle with an area of {3.14 * self.radius * self.radius}cm^2")
        super().describe()

circle = Circle("red", True, 10)

circle.describe()
# Is is a circle with an area of 314.16cm^2
# It is red and filled
```
