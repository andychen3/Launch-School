# https://launchschool.com/exercises/f144e113


"""
rules:

draw method:
1. deals oen card
2. deck should shuffle when initalized
3. if no more cards remain when draw is called the method should generate
a newset of 52 shuffled cards then deal one card from the new card

"""
import random

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.deck = self.create_deck()
        random.shuffle(self.deck)

    def create_deck(self):
        return [Card(rank, suit) for rank in self.RANKS for suit in self.SUITS]

    def draw(self):
        """
        returns the card drawn        
        """
        if self.deck:
            card = self.deck.pop()
        else:
            self.deck = self.create_deck()
            random.shuffle(self.deck)
            card = self.deck.pop()

        return card


class Card:
    def __init__(self, rank, suit):
        self._rank = rank # is the number
        self._suit = suit # suit is the type
        self.rank_dictionary = {2: 2, 3: 3,
                                4: 4, 5: 5, 6: 6, 7: 7,
                                8: 8, 9: 9, 10: 10,
                                "Jack": 11, "Queen": 12,
                                "King": 13, "Ace": 14}

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
            
        return self.rank_dictionary[self.rank] < self.rank_dictionary[other.rank]
    
    def __gt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
            
        return self.rank_dictionary[self.rank] > self.rank_dictionary[other.rank]
    
    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.rank_dictionary[self.rank] == self.rank_dictionary[other.rank]
    
    def __ne__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        
        return self.rank_dictionary[self.rank] != self.rank_dictionary[other.rank]


    def __str__(self):
        """
        Rank of suit
        """
        return f"{self.rank} of {self.suit}"
    
deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).