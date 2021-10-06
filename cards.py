from itertools import product
from random import shuffle


class Card:
    SUITS = ("Spades", "Hearts", "Diamonds", "Clubs")
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']

    def __init__(self, rank, suit, points):
        self.rank = rank
        self.suit = suit
        self.points = points

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck(object):
    def __init__(self):
        self.cards = self._generate_deck()
        shuffle(self.cards)

    def _generate_deck(self):
        points: int
        cards: list = []
        for suit, rank in product(Card.SUITS, Card.RANKS):
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
