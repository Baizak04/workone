user = ("Baizak", 13, False)

age = 14
name = "Baizak"
if name in user:
    print("Пользователь с таким имям найден")
    if age in user:
        print("Пользователь с таким возрастом найден")
    else:
        print("Пользователь с таким возрастом не найден")
else:
    print("Пользователь не найден")
