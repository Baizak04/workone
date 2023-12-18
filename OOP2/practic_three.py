class Cat:
    
    def __init__(self, name: str) -> None:
        self.name = name
        print("Я родился")
    
    def meow(self):
        print("Meow" * 3)
        
    def __repr__(self):
        return f"Я котейка {self.name}"
        
        
barsik = Cat("sar")
print(barsik)