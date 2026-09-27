# Static methods

Static methods are methods that belongs to a class rather than any instance of that class. They are generally used for utility functions

- Instance method -> best for operations on instances of the class
- Static methods -> best for utility functions that do not need access to class data

You access them through the CLASS, not the INSTANCE

```python
class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # instance method, use by accessing an instance of the class.
    # Grabs info from the INSTANCE
    def get_info(self):
        return f"{self.name}: {self.position}"

    # static method.
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

job1 = "Manager"
job2 = "Rocket Scientist"

print(Employee.is_valid_position(job1)) # -> True
print(Employee.is_valid_position(job2)) # -> False
```
