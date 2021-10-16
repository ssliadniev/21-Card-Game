from cards import Deck
from player import Player


class Game:
    """This class represents the gameplay of 21 games."""

    def __init__(self):
        self.deck = Deck()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self) -> None:
        player_status = self.player.deal()
        dealer_status = self.dealer.deal()

        self.player.show_cards()

        if player_status:
            print("Player won! Congrats!")
            if dealer_status:
                print("Dealer and Player won! It's a tie.")
            return

        if self.player_process_game():
            return

        self.dealer.show_cards()
        if player_status:
            print("\nDealer won!")
            return

        if self.dealer_process_game():
            return

        if self.dealer.get_points_of_cards() == self.player.get_points_of_cards():
            print("\nIt's a tie. Better luck next time!")
        elif self.dealer.get_points_of_cards() > self.player.get_points_of_cards():
            print("\nDealer won. Good Game!")
        elif self.dealer.get_points_of_cards() < self.player.get_points_of_cards():
            print("\nPlayer won. Congratulations!")

    def player_process_game(self) -> bool:
        input_action: str = ""
        while input_action != "Stand":
            bust: bool = False
            input_action = input("Hit or Stand?")
            if input_action == "Hit":
                bust = self.player.hit()
                self.player.show_cards()
            if bust:
                print("\nPlayer has lost. Good Game!")
                return True
        return False

    def dealer_process_game(self) -> bool:
        while self.dealer.get_points_of_cards() < 17:
            if self.dealer.hit():
                self.dealer.show_cards()
                print("\nDealer has lost. Congrats!")
                return True
            self.dealer.show_cards()
        return False


if __name__ == "__main__":
    game = Game()
    game.play()
