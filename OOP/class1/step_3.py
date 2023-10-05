# class MyError(Exception):
#     pass

# print(MyError, MyError.mro())

# raise MyError("Ошибка")


class InvalidOperandError(TypeError):
    pass

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return str([self.x, self.y])
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(" \
            f"x={self.x}, y={self.y})"
    def add(self, point: "Point"):
        if not isinstance(point, self.__class__):
            raise InvalidOperandError(
                f"Что-то {self.__class__}, not"
                f" {type(point)}"
            )
        return self.__class__(
            x=self.x + point.x,
            x=self.y + point.y,

        )
        
    def __add__(self, other):
        return self.add(other)
    
    
           
p1 = Point(1, 2)
p2 = Point(x=3, y=4)

print(p1)
print(p2)
print([p1, p2])

p3 = p1 + p2
print(p3)
