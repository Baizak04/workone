foods = []
prices = []
total = 0

while True:
    food = input("Введите продукт для покупки (q - выйти): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Введите цену {food}: $"))
        foods.append((food))
        prices.append(price)
        
print("----- ВАША КОРЗИНА -----")

for food in foods:
    print(food, end=" ")
    
for price in prices:
    total += price

print() 
print(f"Ваша общая сумма составляет: ${total}")
    
    