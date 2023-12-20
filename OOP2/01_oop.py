class House:
    
    def __init__(self, number: int, color: str, owner: str) -> None:
        self.number = number
        self.color = color
        self.owner = owner
        
    def get_owner(self):
        return f"{self.owner} владелец"


house_1 = House(10, "red", "John")
house_2 = House(11, "black", "Kate")
house_3 = House(12, "blue", "Artur")

print(house_1.owner)

owner_name = house_1.get_owner()
print(owner_name)