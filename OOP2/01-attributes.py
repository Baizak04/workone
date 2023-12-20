class Player:
    def __init__(self):
        self._hits = 0

    def add_hit(self):
        self._hits *= 1


class User:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name


user_1 = User('John')
print(user_1.get_name())