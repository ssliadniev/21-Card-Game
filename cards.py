from itertools import product
from random import shuffle, choice

from terminal_playing_cards import Card


class Cards:
    """A deck containing 52 cards."""

    SUITS = ("spades", "hearts", "diamonds", "clubs")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self):
        self.deck = self.generate_deck()
        shuffle(self.deck)

    def generate_deck(self) -> list:
        points: int = 0
        cards: list = []
        for suit, rank in product(self.SUITS, self.RANKS):
            if rank == "A":
                points = 11
            elif rank == "K":
                points = 4
            elif rank == "Q":
                points = 3
            elif rank == "J":
                points = 2
            elif rank.isdigit():
                points = int(rank)
            card = Card(rank, suit, value=points, hidden=False, picture=True)
            cards.append(card)
        return cards

    def get_card(self, amount) -> list:
        cards: list = []
        for _ in range(amount):
            card = choice(self.deck)
            self.deck.remove(card)
            cards.append(card)
        return cards

    def __len__(self):
        return len(self.deck)
