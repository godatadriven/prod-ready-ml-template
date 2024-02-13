import collections

class Deck:
    def __init__(self):
        Card = collections.namedtuple('Card', ['rank', 'suit'])
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
    
    def __getitem__(self, position):
        return self.cards[position]
    
    def __setitem__(self, ind, val):
        self.cards[ind] = val
    
    def __add__(self, other):
        return self.cards + other.cards
    
    def deal(self):
        return self.cards.pop()

class AvatarDeck(Deck):
    ranks = list('23456789T') + ['Sokka', 'Katara', 'Zuko', 'Aang']
    suits = ['Water', 'Air', 'Fire', 'Water']

class French52Deck(Deck):
    ranks = '23456789TJQKA'
    suits = '♠♥♦♣'

    def top_card_is_ace(self):
        return self.cards[-1].rank == 'A'

avatar_deck = AvatarDeck()
deck = French52Deck()

both = deck + avatar_deck
len(both)

# What's the type of `both` in this case?
# type(both)
