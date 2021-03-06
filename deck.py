import random


class Deck:

    def __init__(self):
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.cards_values = (dict(zip(self.cards, self.values)))
        self.full_deck = list(self.cards) * 4
        self.user_hand_values = []
        self.dealer_hand_values = []
        self.make_hand = []
        self.make_user_hand = []
        self.make_dealer_hand = []

    def shuffle(self):
        random.shuffle(self.full_deck)

    def deal_user_hand(self):
        self.make_user_hand = [self.full_deck.pop() for _ in range(2)]
        print(self.make_user_hand)
        for card in self.make_user_hand:
            #if self.make_dealer_hand == ['A', 'A']:
                #self.dealer_hand_values.append(0)
            if card[0:1] == 'A':
                self.cards_values['A'] = 11
            self.user_hand_values.append(self.cards_values[card])
            if sum(self.user_hand_values) < 11:
                self.cards_values['A'] = 11
        print("Your hand:", sum(self.user_hand_values))

    def deal_dealer_hand(self):
        self.make_dealer_hand = [self.full_deck.pop() for _ in range(2)]
        print(self.make_dealer_hand[:1])
        for card in self.make_dealer_hand:
            #if self.make_dealer_hand == ['A', 'A']:
                #self.dealer_hand_values.append(0)
            if card[0:1] == 'A':
                self.cards_values['A'] = 11
            self.dealer_hand_values.append(self.cards_values[card])
            if sum(self.dealer_hand_values) < 11:
                self.cards_values['A'] = 11
        #print("Dealer's hand:", sum(self.dealer_hand_values))























