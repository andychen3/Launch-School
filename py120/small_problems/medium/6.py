# https://launchschool.com/exercises/5a614aef

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
    

# Include Card and Deck classes from the last two exercises.

class PokerHand:
    def __init__(self, deck):
        pass

    def print(self):
       pass

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        pass

    def _is_straight_flush(self):
        pass

    def _is_four_of_a_kind(self):
        pass

    def _is_full_house(self):
        pass

    def _is_flush(self):
        pass

    def _is_straight(self):
        pass

    def _is_three_of_a_kind(self):
        pass

    def _is_two_pair(self):
        pass

    def _is_pair(self):
        pass