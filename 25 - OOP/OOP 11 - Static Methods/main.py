# Static methods -> a method that belongs to a class rather than any object of that class (instance)
#                  They are generally used for utility functions

# Instance method -> best for operations on instances of the class
# Static methods -> best for utility functions that do not need access to class data


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    # instance method, use by accessing an instance of the class
    def get_info(self):
        return f"{self.name}: {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_positions

job1 = "Manager"
job2 = "Rocket Scientist"
print(Employee.is_valid_position(job1))
print(Employee.is_valid_position(job2))

print("-----")

employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


    