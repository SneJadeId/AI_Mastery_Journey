from abc import ABC, abstractmethod
import math

# Abstract Class
class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


# Circle Class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius


# Rectangle Class
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# Test
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Circle Area:", round(circle.calculate_area(), 2))
print("Rectangle Area:", rectangle.calculate_area())