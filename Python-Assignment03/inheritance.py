# Parent Class
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print("Student Information")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Grade: {self.grade}")


# Child Class
class HighSchoolStudent(Student):

    def __init__(self, name, age, grade, grade_level):
        super().__init__(name, age, grade)
        self.grade_level = grade_level

    # Overriding parent method
    def display_info(self):
        print("High School Student Information")
        print(f"Name        : {self.name}")
        print(f"Age         : {self.age}")
        print(f"Grade       : {self.grade}")
        print(f"Grade Level : {self.grade_level}")


# Test
student = HighSchoolStudent("Sneha", 17, "A", 12)
student.display_info()