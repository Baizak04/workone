import random

# Определение класса Card
class Card:
    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit
        
    def get_value(self) -> int:
        if self.rank in "ТВДК": 
            '''ТВДК - ТУЗ, ВАЛТА, ДАМА, КАРОЛЬ'''
            return 10
        else:
            return " A23456789".index(self.rank)
        
    def get_rank(self) -> str:
        return f"{self.suit}{self.rank}"

# Определение класса DeskCard
class DeskCard:
    def __init__(self) -> None:
        _rank = "A23456789ТВДК"
        _suit = "ПБЧК"
        self.__cards = [Card(r, s) for s in _suit for r in _rank]
        random.shuffle(self.__cards)
        
    def get_card(self) -> Card:
        return self.__cards.pop()
    
# Определение класса Player
class Player:
    def __init__(self, name: str) -> None:
        self._hand = []
        self.count = 0
        self.name = name
       
    @property 
    def hand(self) -> str:
        return f"Карты в руке: {', '.join(self._hand)}; Очков - {self.count}"
    
    @hand.setter
    def hand(self, card: Card) -> None:
        self.count += card.get_value()
        self._hand.append(card.get_rank())

# Определение класса Dealer, унаследованного от Player
class Dealer(Player):
    def get_card(self, cards: DeskCard):
        while self.count < 18:
            card = cards.get_card()
            self.hand = card

# Определение класса Game
class Game:
    def __init__(self, player_name: str) -> None:
        self.cards = DeskCard()
        self.player = Player(name=player_name)
        self.dealer = Dealer(name="Dealer")
        
    def print(self) -> str:
        return f'{self.player.name}:\n{self.player.hand}\n{self.dealer.name}:\n{self.dealer.hand}'

    def check_count(self) -> None:
        print(f'{self.player.name}: {self.player.count} очков')
        print(f'{self.dealer.name}: {self.dealer.count} очков')

        if self.player.count > 21:
            print(f'{self.player.name}, вы проиграли')
        elif self.dealer.count > 21 and self.player.count <= 21:
            print(f'{self.player.name}, вы победили!')
        elif self.dealer.count == self.player.count:
            print('Ничья')
        elif self.dealer.count > self.player.count:
            print(f'{self.player.name}, вы проиграли')
        elif self.dealer.count < self.player.count:
            print(f'{self.player.name}, вы победили!')

    def start(self) -> None:
        self.player.hand = self.cards.get_card()
        self.player.hand = self.cards.get_card()
        
        self.dealer.hand = self.cards.get_card()
        self.dealer.hand = self.cards.get_card()
        
        while self.player.count < 21:
            print(self.print())
            answer = input("Карту? yes/no ")
            if answer == "yes":
                self.player.hand = self.cards.get_card()
            elif answer == "no":
                self.dealer.get_card(self.cards)
                break

        print(self.print())
        self.check_count()

def main() -> None:
    name = input("Введите ваше имя: ")
    game = Game(name)
    game.start()

if __name__ == '__main__':
    main()