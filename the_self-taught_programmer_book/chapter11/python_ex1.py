# 1)
# class Orange:
#     def __init__(self, weight, color):
#         self.weight = weight
#         self.color = color
#         print("Создано")
        
        
# fruit1 = Orange(10, "yellow")
# fruit2 = Orange(20, "green")
# fruit1.color = "black"
# fruit2.weight = 30
# print(fruit1.color)
# print(fruit2.weight)

# 2)
class Orange:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        self.mold = 0
        print("Создано")
        
    def rot(self, days, temp):
        self.mold = days * temp
        
        
fruit = Orange(3, "Апельсин")
print(fruit.mold)
fruit.rot(10, 22)
print(fruit.mold)

# 3)
class Rectangle:
    def __init__(self, width, len) -> int:
        self.width = width
        self.len = len
        
    def area(self):
        return self.width * self.len
    
    def change_size(self, width, len):
        self.width = width
        self.len = len
        
        
rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())