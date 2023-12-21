from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items, company):
        self.items = items
        self.company = company
        
    @abstractmethod
    def add(self, title, count):
        pass
    
    @abstractmethod
    def remove(self, title, count):
        pass
    
    @property
    def get_free_space(self):
        pass
    
    @property
    @abstractmethod
    def items(self):
        pass
    
    @property
    @abstractmethod
    def get_unique_items_count(self):
        pass
    

class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100
        
    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count
        
    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity
    
    @property
    def items(self):
        return self._items
    
    @items.setter
    def _items(self, new_items):
        self._items = new_items
    
    @property
    def get_unique_items_count(self):
        return len(self._items.keys())
    
    
class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20
        
        
class Request:
    def __init__(self, info):
        self.info = self._split_info(info)
        self.from_ = info[4]
        self.to = info[6]
        self.amount = info[1]
        self.product = info[2]
    
    @staticmethod
    def _split_info(info):
        return info.split(" ")
    
    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"
    
    
def main():
    while(True):
        user_input = input("Введите запрос: ") 
        user_input = "Доставить 3 печеньки из склад в магазин"
        
        if user_input == "stop":
            break
        
        store = Store()
        shop = Shop()
        request = Request(user_input)

        store_items = {
            'чипсы': 10,
            'сок': 20,
            'кофе': 7,
            'печеньки': 18,
        }

        store.items = store_items
        
        print(store_items)
        
        break
        

if __name__ == "__main__":
    main()