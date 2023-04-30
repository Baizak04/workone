from oop_2 import Verification

class V2(Verification):
    
    def __init__(self):
        print('w')
        
    def save(self):
        with open('users') as r:
            for i in r:
                if f'{self.login, self.password}' + '\n' == i:
                    raise ValueError ('такой есть')
        Verification.save(self)
        
    def show(self):
        return self.login, self.password
    
    
x = V2('kenny', '12323112')
x.save()