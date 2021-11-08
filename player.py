from cards import Cards


class Player:
    """This class represents a player in a 21 game."""

    def __init__(self, isDealer):
        self.cards: list = []
        self.isDealer: bool = isDealer
        self.name: str
        self.score: float = self.get_points()
        self.in_game: bool = True

    def hit(self, cards) -> None:
        self.cards.extend(cards)
        self.get_points()

    def get_name(self, number):
        if self.isDealer:
            self.name = "Dealer"
        else:
            self.name = input(f"Enter name of player {number + 1}:")
        return self.name

    def get_points(self) -> float:
        self.score = Cards.get_cards_points(self.cards)
        return self.score

    def show_cards(self) -> None:
        print(f"\n{self.name}'s cards:")
        Cards.get_view_cards(self.cards)
        print(f"Score: {self.score}")
