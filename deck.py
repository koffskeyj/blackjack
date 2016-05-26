import random
# from hand import Hand


class Deck:

    def __init__(self):
        self.suits = ["H", "D", "C", "S"]
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.full_deck = []
        for suit in self.suits:
            for card in self.cards:
                self.full_deck.append(suit + card)

    def draw_hand(self):
        pass


deck = Deck()
deck.draw_hand()






