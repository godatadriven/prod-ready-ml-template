class AvatarDeck(Deck):
    ranks = list('23456789') + ['Toph', 'Sokka', 'Katara', 'Zuko', 'Aang']
    suits = ['Water', 'Air', 'Fire', 'Earth']
    
avatar_deck = AvatarDeck()
avatar_deck.cards
