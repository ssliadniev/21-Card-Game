from cards import Cards
from player import Player
from random import choice


class Game:
    """This class represents the gameplay of 21 games."""

    def __init__(self):
        self.deck = Cards()
        self.players = self.set_players()
        self.playing = True

    def play(self) -> None:
        while self.playing:
            self.players = list(filter(lambda player: (player.ingame), self.players))
            for player in self.players:
                player.show_cards()
                self.player_process_game(player)
                if player.score > 21:
                    player.ingame = False
                    print(f"{player.name} leaves the game.")
                elif player.score == 21:
                    print(f"{player.name} won!")
                    self.playing = False

    @staticmethod
    def set_players():
        while True:
            try:
                number_players = int(input("Please, enter number of players: "))
                assert number_players > 0
                break
            except:
                print("Nope")
        players = [Player(False) for _ in range(number_players)]
        players.append(Player(True))
        for index, player in enumerate(players):
            player.name = player.get_name(index)
            player.hit(2)
        return players

    @staticmethod
    def player_process_game(player):
        available_actions = ("hit", "stand")
        if player.isDealer:
            dealer_action = choice(["hit", "stand"])
            if dealer_action == "hit":
                player.hit(1)
                player.show_cards()
            elif dealer_action == "stand":
                print("Dealer stood.")
        else:
            while True:
                player_action = input("Hit or Stand?").lower()
                if player_action in available_actions:
                    break
            if player_action == "hit":
                player.hit(1)
                player.show_cards()
            elif player_action == "stand":
                print(f"{player.name} stood.")


if __name__ == "__main__":
    game = Game()
    game.play()
