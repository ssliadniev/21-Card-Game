from terminal_playing_cards import View
from cards import Cards


class Player:
    """This class represents a player in a 21 game."""

    def __init__(self, isDealer):
        self.cards: list = []
        self.isDealer: bool = isDealer
        self.name: str
        self.score: int = self.get_points_of_cards()
        self.ingame: bool = True

    def hit(self, number) -> None:
        deck = Cards()
        self.cards.extend(deck.get_card(number))
        self.get_points_of_cards()

    def get_name(self, number):
        if self.isDealer:
            self.name = "Dealer"
        else:
            self.name = input(f"Enter name of player {number + 1}:")
        return self.name

    def get_points_of_cards(self) -> int:
        self.score = sum([card.value for card in self.cards])
        return self.score

    def show_cards(self) -> None:
        if self.isDealer:
            print(f"\nDealer's cards:")
        else:
            print(f"\n{self.name}'s cards:")
        print(View(self.cards))
        print(f"Score: {self.score}")
