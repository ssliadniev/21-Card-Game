from terminal_playing_cards import View


class Player:
    """This class represents a player in a 21 game."""

    def __init__(self, isDealer):
        self._cards: list = []
        self.isDealer: bool = isDealer
        self.score: int = 0

    def hit(self, card):
        self._cards.extend(card)
        self.get_points_of_cards()
        if self.score > 21:
            return True
        return False

    def get_points_of_cards(self):
        self.score = sum([card.points for card in self._cards])
        return self.score

    def show(self):
        if self.isDealer:
            print("Dealer's cards")
        else:
            print("Players cards")
        cards_view = View([card.card for card in self._cards])
        print(cards_view)
        print(f"Score: {self.score}")
