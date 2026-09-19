# Class Attribute - variable defined directly in the class.
#                  they are defined outside of the constructor
#                  it is shared among all instances of that class (objects)
#                  allows you to share data among all instances of the class


class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

        # you can apply logic to class variables
        Student.num_students += 1

student1 = Student("Dylan", 15)
student2 = Student("John", 14)

print(student1.class_year) # both share the same class_year, note to NOT do it this way however                  
print(student2.class_year) # use below instead

print(Student.class_year) # good practice to access through the class instead of an instance
print(Student.num_students) # updates every time the constructor is run / every object created


print(f"Graduating year of {Student.class_year} has {Student.num_students} students")
