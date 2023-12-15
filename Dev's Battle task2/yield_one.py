try:
    def test():
        for i in range(2):
            yield i


    a = test()
    print(next(a))
    print(next(a))
    print(next(a))
    print(next(a))
    
except StopIteration:
    print("Stop") 
finally:
    print("The end")     
    
    
# 2)
def test():
    print("started")
    while True:
        yield 1
        yield 2
        
        
a = test()
print(next(a))
print(next(a))
print(next(a))
