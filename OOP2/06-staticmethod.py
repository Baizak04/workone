class PlayerRecord:
    
    @staticmethod
    def get_top_10(self):
        pass
    
    @staticmethod
    def get_top_100(self):
        pass
    
    @staticmethod
    def add_record(self, record):
        pass
    
    
# top_10 = PlayerRecord.get_top_10()


class Cat:
    
    def say(self):
        self.what_does_cat_say()
        
    @staticmethod
    def what_does_cat_say():
        print("Meow")
        
        
Cat.what_does_cat_say()

cat = Cat()
cat.what_does_cat_say()

cat = Cat()
cat.say()