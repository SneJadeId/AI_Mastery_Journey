class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        print(f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}")


class HighSchoolStudent(Student):

    def __init__(self, name, age, grade, school):
        super().__init__(name, age, grade)
        self.school = school

    def display_info(self):
        print(f"High School Student: {self.name}, Age: {self.age}, Grade: {self.grade}, School: {self.school}")


# Polymorphic function
def print_student_info(student):
    student.display_info()


# Test
student1 = Student("Reya", 11, "B")
student2 = HighSchoolStudent("Sneha", 30, "A", "VPNCPS")

print_student_info(student1)
print_student_info(student2)