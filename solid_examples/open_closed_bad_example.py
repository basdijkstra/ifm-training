import math


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

class Circle:
    def __init__(self, radius):
        self.radius = radius

# This is a bad example, because if we want to extend this to allow for
# more shapes, we need to modify the AreaCalculator class.
# So, it's not open for extension yet.
class AreaCalculator:
    def calculate_area(self, shapes: list[object]):
        area = 0
        for shape in shapes:
            if isinstance(shape, Rectangle):
                area += (shape.length * shape.width)
            elif isinstance(shape, Circle):
                area += shape.radius * shape.radius * math.pi
        print(f'Area: {area}')

if __name__ == "__main__":
    area_calculator = AreaCalculator()
    area_calculator.calculate_area([Rectangle(3, 5), Rectangle(4, 4), Circle(5)])
