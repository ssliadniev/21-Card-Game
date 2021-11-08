import time
from random import randint

from cards import Cards
from player import Player


class Game:
    """This class represents the gameplay of 21 games."""

    def __init__(self):
        self.deck = Cards()
        self.players = self.set_players()
        self.playing = True

    def play(self) -> None:
        while self.playing:
            self.players = list(filter(lambda player: (player.ingame), self.players))
            if len(self.players) == 1:
                print(f"{self.players[0].name} won!")
                break
            for player in self.players:
                player.show_cards()
                self.player_process_game(player)
                if player.score > 21:
                    player.in_game = False
                    print(f"{player.name} leaves the game.")
                elif player.score == 21:
                    print(f"{player.name} won!!")
                    self.playing = False

    def set_players(self):
        while True:
            try:
                number_players = int(input("Please, enter number of players: "))
                assert number_players > 0
                break
            except:
                print("Nope")
        players = [Player(isDealer=False) for _ in range(number_players)]
        players.append(Player(isDealer=True))
        for index, player in enumerate(players):
            player.name = player.get_name(index)
            player.hit(cards=self.deck.get_cards(amount=2))
        return players

    def player_process_game(self, player):
        available_actions = ("hit", "stand")
        if player.isDealer:
            time.sleep(randint(1, 6))
            if player.score <= 17:
                player.hit(cards=self.deck.get_cards())
                player.show_cards()
            elif player.score > 17:
                print("Dealer stood.")
        else:
            while True:
                player_action = input("Hit or Stand?").lower()
                if player_action in available_actions:
                    break
            if player_action == "hit":
                player.hit(cards=self.deck.get_cards())
                player.show_cards()
            elif player_action == "stand":
                print(f"{player.name} stood.")


if __name__ == "__main__":
    game = Game()
    game.play()
