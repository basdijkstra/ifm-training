import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

# This is a much better example, because if we want to extend this to allow for
# more shapes, all we need to do is add another class that extends the abstract
# Shape class, without having to modify the AreaCalculator.
class AreaCalculator:
    def calculate_area(self, shapes: list[Shape]):
        area = 0
        for shape in shapes:
            area += shape.area()
        print(f'Area: {area}')

if __name__ == "__main__":
    area_calculator = AreaCalculator()
    area_calculator.calculate_area([Rectangle(3, 5), Rectangle(4, 4), Circle(5)])
