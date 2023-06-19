menu = {"шаурма": 170.00,
        "ход-дог": 120.00,
        "гамбургер": 150.00,
        "двойной шаурма": 200.00,
        "картошка фри": 80.00,
        "запеченый шаурма": 180.50,
        "шаурдог": 140.00,
        "коко-кола-1л": 70.25,
        "коко-кола-1.5л": 100.00,
        "коко-кола-2л": 120.00,
        "компот-1л": 45.00
        }

cart = []
total = 0

print("------ MENU ------")
for key, value in menu.items():
    print(f"{key:10}: ${value: .2f}")
print("------------------")

while True:
    food = input("Выберите из меню еду и напитку (Чтобы выйти нажмите q): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print("---- ВАШ ЗАКАЗ ----")
for food in cart:
    total += menu.get(food)
    print(food, end=" ")
    
print()
print(f"Общая сумма: ${total: .2f}")