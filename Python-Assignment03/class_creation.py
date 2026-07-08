# Class Creation

class Student:
    # Constructor to initialize student details
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to display student information
    def display_info(self):
        print("Student Information")
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"Grade: {self.grade}")


# Test
student1 = Student("Sneha", 22, "A")
student1.display_info()

