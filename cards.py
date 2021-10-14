from itertools import product
from random import shuffle

from terminal_playing_cards import Card


class Cards:
    """A card object, which have a suit and rank."""

    SUITS = ("spades", "hearts", "diamonds", "clubs")
    RANKS = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, rank, suit, points):
        self.card = Card(rank, suit, value=points, hidden=False, picture=True)

    def __str__(self):
        return f"{self.card}"


class Deck(object):
    """A deck containing 52 cards."""

    def __init__(self):
        self.deck = self.generate_deck()
        shuffle(self.deck)

    @staticmethod
    def generate_deck():
        points: int = 0
        cards: list = []
        for suit, rank in product(Cards.SUITS, Cards.RANKS):
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
            card = Cards(rank, suit, points)
            cards.append(card)
        return cards

    def get_cards(self):
        return [self.deck.pop() for _ in range(2)]

    def __len__(self):
        return len(self.deck)
