from deck import Deck
from blackjack import Blackjack


class Game:
    def __init__(self):

        deck = Deck()
        deck.shuffle()
        deck.deal_dealer_hand()
        deck.deal_user_hand()
        self.hit_value = []
        self.dealer_hit_value = []
        self.user_hit_or_stay = ""
        self.user_hit = []
        self.dealer_hit = []

        def play_again():
            self.user_input = input("Would you like to play again? y/n ")
            if self.user_input == "y":
                Game()
            else:
                exit()

        def total():
            print("Dealer's total:", sum(deck.dealer_hand_values + self.dealer_hit_value))
            print("Your total:", sum(deck.user_hand_values + self.hit_value))

        while True:

            if sum(deck.user_hand_values) == 21:
                print("Blackjack! You win!")
                play_again()
            if sum(deck.dealer_hand_values) == 21:
                print("Blackjack! Dealer wins!")
                play_again()

            self.user_hit_or_stay = input("Would you like to hit or stay? hit/stay: ")

            if self.user_hit_or_stay == "hit":
                if sum(deck.user_hand_values + self.hit_value) >= 11:
                    deck.cards_values['A'] = 1
                self.user_hit = [deck.full_deck.pop() for _ in range(1)]
                print("You hit:", self.user_hit)
                for card in self.user_hit:
                    self.hit_value.append(deck.cards_values[card])
                    print("Your total is:", sum(deck.user_hand_values + self.hit_value))
                    if sum(deck.user_hand_values + self.hit_value) > 21:
                        print("Bust!")
                        total()
                        play_again()
            else:
                print("You stay.")

            if sum(deck.dealer_hand_values) < 17:
                if sum(deck.dealer_hand_values + self.dealer_hit_value) >= 11:
                    deck.cards_values['A'] = 1
                self.dealer_hit = [deck.full_deck.pop() for _ in range(1)]
                print("Dealer Hit: ", self.dealer_hit)
                for card in self.dealer_hit:
                    self.dealer_hit_value.append(deck.cards_values[card])
                    if sum(deck.dealer_hand_values + self.dealer_hit_value) > 21:
                        print("Dealer Busts! You win!")
                        total()
                        play_again()

            if sum(deck.dealer_hand_values + self.dealer_hit_value) >= 17:

                if self.user_hit_or_stay == "hit":
                    continue

                elif sum(deck.dealer_hand_values + self.dealer_hit_value) < sum(deck.user_hand_values + self.hit_value):
                    print("You win!")
                    total()
                    play_again()
                elif sum(deck.dealer_hand_values + self.dealer_hit_value) == sum(deck.user_hand_values + self.hit_value):
                    print("Draw!")
                    total()
                    play_again()
                else:
                    print("Dealer wins!")
                    total()
                    play_again()

Blackjack()
Game()

