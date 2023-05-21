class Women:
    def __init__(self, age):
        self.age = age
        
        
    def say_hello(self):
        print("hello, i am {}".format(self.age))
        
        
women = Women(age=48)
women.say_hello()

