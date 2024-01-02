import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * math.pi

a_circle = Circle(4)
print(a_circle.calculate_area())


# 2)
class Triangle:
    def __init__(self, r, a):
        self.r = r
        self.a = a
        
    def area(self):
        return self.r * self.a // 2
    

b_triangle = Triangle(2, 3)
print(b_triangle.area())