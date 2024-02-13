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
    
    def __len__(self):
        return len(self.cards)
        
    def __str__(self):
        return f'Deck(suits={self.suits}, ranks={self.ranks})'
    
    def deal(self):
        dealt_card = self.cards.pop()
        self.dealt_cards.append(dealt_card)
        return dealt_card
    
    def check_ace(self):
        return self.cards[-1].rank == 'A'
    
deck = Deck()
print(deck)