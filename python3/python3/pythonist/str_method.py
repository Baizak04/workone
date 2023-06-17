# 1)
str_method = 'python hi'
print(str_method.capitalize())

# 2)
str_method1 = 'python'
print(str_method1.upper())

# 3)
str_method2 = 'python hi'
print(str_method2.title())

# 4)
str_method3 = 'PYTHON'
print(str_method3.casefold())

# 5)
str_method4 = "python"
txt = str_method4.center(20, "-")
print(txt)

# 6)
str_method5 = 'python hhhi'
print(str_method4.count('h'))

# 7)
sentence = "Hello, welcome to my world."
print(sentence.endswith("."))

# 8)
sentence = "H\te\tl\tl\to"
print(sentence.expandtabs(1))
print(sentence.expandtabs(2))
print(sentence.expandtabs(3))
print(sentence.expandtabs(4))
print(sentence.expandtabs(5))

# 9)
sentence = "Hello world"
x = sentence.find("world")
print(x)

# 10)
data = {"name": "John", "age": 21}
sentence = "My name is {name} and I am {age} years old".format_map(data)
print(sentence)
