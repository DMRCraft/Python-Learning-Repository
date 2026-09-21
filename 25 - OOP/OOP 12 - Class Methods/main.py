# Class methods - allows operations related to the class itself
#                 takes (cls) as its first parameter, representing the class itself


class Student:
    count = 0
    total_gpa_count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa_count += gpa

    # instance method
    def get_info(self):
        return f"{self.name}: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"The total number of students is {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"The average gpa is {cls.total_gpa_count / cls.count:.2f}"

    



print(Student.get_count())
print("---")

student1 = Student("Dylan", 3.5)
student2 = Student("John", 2.7)
student3 = Student("Alex", 4.0)

print(Student.get_count())
print(Student.get_average_gpa())