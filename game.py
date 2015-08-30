import itertools
import functools
import random
from enum import IntEnum

class Suit(IntEnum):
    hearts   = 4
    diamonds = 3
    clubs    = 2
    spades   = 1


class Value(IntEnum):
    joker = 15
    ace   = 14
    king  = 13
    queen = 12
    jack  = 11
    ten   = 10
    nine  = 9
    eight = 8
    seven = 7
    six   = 6
    five  = 5
    four  = 4
    three = 3
    two   = 2


class Game500:
    def __init__(self):
        self.deck = []
        self._init_deck()

    def _init_deck(self):
        """ Initialise the deck to have all cards minus one joker;
            and all the twos, threes, and black fours."""
        # Red fours
        self.deck.append((Suit.hearts, Value.four))
        self.deck.append((Suit.diamonds, Value.four))

        # Joker
        self.deck.append((None, Value.joker))

        # Everything else
        for value in map(Value, range(5,15)):
            for suit in Suit:
                self.deck.append((suit, value))

        # shuffffle
        random.shuffle(self.deck)
