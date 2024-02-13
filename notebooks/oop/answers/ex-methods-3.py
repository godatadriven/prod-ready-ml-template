class Deck:
    ranks = '23456789TJQKA'
    suits = '♠♥♦♣'
    
    def __init__(self):
        self.cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
        self.dealt_cards = []
    
    def deal(self):
        dealt_card = self.cards.pop()
        self.dealt_cards.append(dealt_card)
        return dealt_card
    
    def size(self):
        return len(self.cards)
    
    def top_card_is_ace(self):
        return self.cards[-1].rank == 'A'
    
deck = Deck()
deck.deal()
deck.dealt_cards