from random import shuffle

class Dealer():
    
    def __init__(self, deck, num_cards=0):
        self.deck = deck
        shuffle(self.deck)
        self.num_cards = num_cards
        
    def deal_hand(self):
        return [self.deck.deal() for n in range(self.num_cards)]

gofish = Dealer(French52Deck(), 7)

gofish.deal_hand()