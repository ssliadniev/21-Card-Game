from terminal_playing_cards import View
from cards import Cards


class Player:
    """This class represents a player in a 21 game."""

    def __init__(self, isDealer):
        self.cards: list = []
        self.isDealer: bool = isDealer
        self.name = self.get_name()
        self.score: int = 0

    def hit(self) -> bool:
        deck = Cards()
        self.cards.extend(deck.get_card(1))
        self.get_points_of_cards()
        if self.score > 21:
            return True
        return False

    def deal(self) -> bool:
        deck = Cards()
        self.cards.extend(deck.get_card(2))
        self.get_points_of_cards()
        if self.score == 21:
            return True
        return False

    def get_name(self):
        if self.isDealer:
            self.name = input("Your name: ")
        else:
            self.name = "Dealer"
        return self.name

    def get_points_of_cards(self) -> int:
        self.score = sum([card.value for card in self.cards])
        return self.score

    def show_cards(self) -> None:
        if self.isDealer:
            print("\nDealer's cards:")
        else:
            print("\nPlayers cards:")
        print(View(self.cards))
        print(f"Score: {self.score}")
