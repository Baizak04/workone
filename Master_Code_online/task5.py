from typing import Optional
from dataclasses import dataclass

@dataclass
class Foo:
    id: Optional[int] = None
    

print(Foo())

# 2)
def execute(class_):
    def wrapper():
        return class_
    
    return wrapper

@execute
class A:
    pass


print(type(A()))

# 3)
import builtins


def sum(*args):
    return builtins.sum(args + (1,))


print(sum(1, 2, 3))

# 4)
# x = lambda: pass
# print(x())

# 5)
# try:
#     import orjson as json
# except ImportError:
#     import json
    
    
# print(json.__name__)

# 6)
for i in range(3):
    print(i)
    i = 0