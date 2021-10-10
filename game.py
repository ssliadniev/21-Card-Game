from cards import Deck
from player import Player, Dealer


class Game:

    def __init__(self):
        self._deck = Deck()
        self._player = Player()
        self._dealer = Dealer()

    def _print_actions(self):
        print("Availabes actions:\n1. Hit card.\n2.Stands.\n3.Quit.")

    def _start_game(self):
        game_over = False
        self._print_actions()
        while not game_over:
            self._play_game()

    def _play_game(self):
        self._play_game(self._player)
        self._play_game(self._dealer)

    def hit_card(self, player):
        player.add_card(self.deck.get_cards(1))
        self.deck.print_cards(player)
        if player.check_sum():
            self.output(player, "Sum of cards goes over 21! Player lost!")
            player.is_stand = True
            player.is_lose = True
            self.is_active = False

    def stand(self, player):
        self.output(player, "Stands!")
        player.is_stand = True

    def quit(self, player):
        self.output(player, "Quit the game!")
        player.is_stand = True
        player.is_lose = True
        self.is_active = False

    def find_winner(self):
        candidates = [player for player in self.players if not player.is_lose]
        if len(candidates) == 1:
            print(f"*  {candidates[0].name} - WINNER!  *")
        else:
            winner = max(candidates, key=lambda player: player.sum_of_cards)
            print(f"*  {winner.name} - WINNER!  *")
        self.is_active = False

    def output(self, curr_player, text):
        print(f"[{curr_player.name}] {text} \n")