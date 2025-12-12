import collections
from random import shuffle


class Deck:
    def __init__(self, name):
        self.name = name

        Card = collections.namedtuple('Card', ['rank', 'suit'])
        self._cards = [
            Card(rank, suit)
            for suit in self.suits
            for rank in self.ranks
        ]
        self.dealt_cards = []
   
    def __len__(self):
        return len(self._cards)
        
    def __str__(self):
        return f'Deck(suits={self.suits}, ranks={self.ranks})'
    
    def __getitem__(self, position):
        return self._cards[position]
    
    def __setitem__(self, ind, val):
        self._cards[ind] = val
    
    def __add__(self, other):
        return self._cards + other._cards

    def __gt__(self, other):
        if self.__class__ == other.__class__:
            return self.num_j_q_k > other.num_j_q_k
        
        return NotImplemented

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.num_j_q_k < other.num_j_q_k
        
        return NotImplemented
         
    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.num_j_q_k == other.num_j_q_k
        
        return NotImplemented

    @property
    def num_j(self):
        return len([card for card in self._cards if card.rank == 'J'])

    @property
    def num_q(self):
        return len([card for card in self._cards if card.rank == 'Q'])

    @property
    def num_k(self):
        return len([card for card in self._cards if card.rank == 'K'])

    @property
    def num_j_q_k(self):
        return self.num_j + self.num_q + self.num_k
    
    def win(self, other):
        """Determine winner and print result. Returns winner name or None for draw."""
        # Primary comparison: total face cards
        if self > other:
            print(f"{self.name} wins with {self.num_j_q_k} face cards (J, Q, K)")
            return self.name
        elif self < other:
            print(f"{other.name} wins with {other.num_j_q_k} face cards (J, Q, K)")
            return other.name

        # Tiebreaker: check K, Q, J in order
        for rank, count_attr in [('K', 'num_k'), ('Q', 'num_q'), ('J', 'num_j')]:
            self_count = getattr(self, count_attr)
            other_count = getattr(other, count_attr)

            if self_count > other_count:
                print(f"{self.name} wins with {self_count} {rank}s")
                return self.name
            elif self_count < other_count:
                print(f"{other.name} wins with {other_count} {rank}s")
                return other.name

        # All counts equal - draw
        print(f"{self.name} reaches a draw with {other.name}")
        return None
    
    def deal(self):
        return self._cards.pop()


class French52Deck(Deck):
    ranks = '23456789TJQKA'
    suits = '♠♥♦♣'

    def top_card_is_ace(self):
        return self.cards[-1].rank == 'A'

deck1 = French52Deck('Tom')
deck2 = French52Deck('Jerry')

print(f"Shuffling the cards for {deck1.name} and {deck2.name}...")
shuffle(deck1)
shuffle(deck2)

for i in range(15):
    deck1.deal()
    deck2.deal()

print(f"After discarding 15 cards, there are {len(deck1)} cards for {deck1.name} and {len(deck2)} cards for {deck2.name}.")

print(f"{deck1.name} has {deck1.num_j_q_k} face cards (J, Q, K) with {deck1.num_j} Js, {deck1.num_q} Qs, {deck1.num_k} Ks.")
print(f"{deck2.name} has {deck2.num_j_q_k} face cards (J, Q, K) with {deck2.num_j} Js, {deck2.num_q} Qs, {deck2.num_k} Ks.")

winner = deck1.win(deck2)
print(f"The winner is {winner}")