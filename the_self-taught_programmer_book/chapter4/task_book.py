def foo1(x: int):
    return x ** 2


result = foo1(2)
print(result)


# 2)
def str1(str_one: str):
    return str_one


result = str1("hello")
print(result)


# 3)
def pas1(int1: int):
    return int1 // 2

def pas2(int2: int):
    return int2 * 4


result1 = pas1(2)
result2 = pas2(result1)
print(result2)


# 5)
def foo(str1: str):
    try:
        return float(str1)
    except ValueError:
        print("Преобразовние строку на вещественного число невозможно это у нас ошибка ")
        
        
result = foo("hi")
print(result)