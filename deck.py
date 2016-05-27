import random
# from hand import Hand


class Blackjack:

    def __init__(self):
        print("Welcome to Blackjack!")





class Deck:

    def __init__(self):
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards_values = dict(zip(self.cards, self.values))
        self.full_deck = list(self.cards) * 4
        self.hand_values = []
        self.make_hand = []

    def shuffle(self):
        random.shuffle(self.full_deck)

    def deal_hand(self):
        self.make_hand = [self.full_deck.pop() for _ in range(2)]
        print(self.make_hand)
        for card in self.make_hand:
            self.hand_values.append(self.cards_values[card])
        print("Your total is:", sum(self.hand_values))




class Game:



    def __init__(self):

        deck = Deck()
        deck.shuffle()
        deck.deal_hand()
        self.hit_value = []



        while True:

            self.hit_or_stay = input("Would you like to hit or stay? y/n: ")

            if self.hit_or_stay == "y":
                self.hit = [deck.full_deck.pop() for _ in range(1)]
                print(self.hit)
                for card in self.hit:
                    self.hit_value.append(deck.cards_values[card])
                    print("Your total is:", sum(deck.hand_values + self.hit_value))

            elif self.hit_or_stay == "n":
                print("You stay.")
                break



game = Game()
game.play()








