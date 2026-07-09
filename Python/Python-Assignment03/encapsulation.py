# Encapsulation Example

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.__age = age      # Private attribute
        self.grade = grade

    # Setter method
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

    # Getter method
    def get_age(self):
        return self.__age

    def display_info(self):
        print("Student Information")
        print(f"Name : {self.name}")
        print(f"Age  : {self.__age}")
        print(f"Grade: {self.grade}")


# Test
student = Student("Sneha", 22, "A")

student.display_info()

student.set_age(23)

print("Updated Age:", student.get_age())