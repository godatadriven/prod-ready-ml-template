class Deck:
    ranks = '23456789TJQKA'
    suits = '♠♥♦♣'
    
    def __init__(self):
        self.cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
            
    def deal(self):
        return self.cards.pop()
    
    def size(self):
        return len(self.cards)
    
deck = Deck()
deck.size()