from cards import Deck, Card
import time
from typing import Optional


class Player:
    """This class represents a player in a 21 game."""

    def __init__(self, cards: list):
        self._cards: list = cards
        self.action: classmethod = self.get_player_action()
        self.points: int = self.get_points_of_cards()
        self.is_stand: bool = False
        self.is_lose: bool = False

    def get_player_action(self, decision: Optional[str, None] = None):
        actions = {
            "1": "",
            "2": ""
        }
        action = actions.get(decision)
        if action is None:
            action = self.get_player_action('Make your decision = ')
        return action

    def hit(self, card):
        self._cards.append(card)
        self.points = self.get_points_of_cards()

    def get_points_of_cards(self):
        points: int = sum([card.points for card in self._cards])
        return points

    def has_21(self):
        return self.get_points_of_cards() > 21

    def get_card(self):
        return self._cards


class Dealer(Player):

    def __init__(self, cards):
        super().__init__("Dealer", cards)

    def _make_action(self):
        if self.points < 17:
            return super(Dealer, self).get_player_action("1")
        else:
            return super(Dealer, self).get_player_action("2")
