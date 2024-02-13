class Deck:
    ranks = '23456789TJQKA'
    suits = '♠♥♦♣'
    
    def __init__(self, debug_value = False):
        self.__cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
   
    def __len__(self):
        return len(self.__cards)
        
    def __str__(self):
        return f'Deck(suits={self.suits}, ranks={self.ranks})'
    
    def __getitem__(self, position):
        return self.__cards[position]
    
    def __setitem__(self, ind, value):
        self.__cards[ind] = value
    
    def deal(self):
        return self.__cards.pop()
    
    def check_ace(self):
        return self.__cards[-1].rank == 'A'
    
    @property
    def cards(self):
        return self.__cards
        
deck = Deck()