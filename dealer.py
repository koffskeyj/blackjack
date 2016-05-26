from deck import Deck
import random


class Dealer:

    def __init__(self):
        self.dealer_deck = Deck().full_deck
        random.shuffle(self.dealer_deck)

    def deal_hand(self):
        self.make_hand = [self.dealer_deck.pop() for _ in range(2)]
        print(self.make_hand)
        print(self.dealer_deck)

dealer = Dealer()
dealer.deal_hand()