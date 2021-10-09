from itertools import product
from random import shuffle

from terminal_playing_cards import Card


class Cards:
    """A card object, which have a suit and rank."""

    SUITS = ("spades", "hearts", "diamonds", "clubs")
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

    def __init__(self, rank, suit, points):
        self.rank = rank
        self.suit = suit
        self.points = points
        self.image = Card(rank, suit[0])

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck(object):
    """A deck containing 52 cards."""

    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        points: int
        cards: list = []
        for suit, rank in product(Cards.SUITS, Cards.RANKS):
            if rank == "Ace":
                points = 11
            elif rank == "King":
                points = 4
            elif rank == "Queen":
                points = 3
            elif rank == "Jack":
                points = 2
            elif rank.isdigit():
                points = int(rank)
            card = Card(rank, suit, points)
            cards.append(card)
        return cards

    def get_card(self):
        if len(self) == 0:
            return None
        else:
            return self.cards.pop()

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        self.result = ''
        for c in self.cards:
            self.result = self.result + str(c) + '\n'
        return self.result
