class A:
    MAIN_NAME = "Name A"
    
    def __new__(cls, *args, **kwargs) -> None:
        isinstance = super(A, cls).__new__(cls)
        return isinstance
    
    def __init__(self, name: str) -> None:
        self.name = name
    
    
a = A("Test")
print(a.MAIN_NAME)
print(a.name)