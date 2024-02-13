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
    
    def top_card_is_ace(self):
        return self.cards[-1].rank == 'A'

deck = Deck()
deck.top_card_is_ace()