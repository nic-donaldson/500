import itertools
import functools
import random
from enum import IntEnum, Enum


class IllegalMoveException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return "{} is not a valid move at this time".format(self.value)


class GamePhase(Enum):
    bid      = 1
    inround  = 2
    score    = 3
    postgame = 4
    gameover = 5


class Player(Enum):
    north = 1
    east  = 2
    south = 3
    west  = 4


class Suit(IntEnum):
    notrump  = 5
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


class Command:
    def __init__(self, name):
        self.name = name

    def execute(self, game):
        raise NotImplemented


class StartCommand(Command):
    def __init__(self):
        Command.__init__(self, "start")

    def execute(self, game):
        game.start()


class BidCommand(Command):
    def __init__(self, player, bid):
        self.player = player
        self.bid = bid
        Command.__init__(self, "bid {} {}".format(player, bid))

    def execute(self, game):
        game.bid(self.player, self.bid)


class Game500:
    northsouth = (Player.north, Player.south)
    eastwest = (Player.east, Player.west)

    def __init__(self):
        self.deck   = []    # [(Value,Suit)]
        self.hands  = {}    # Player -> [(Value, Suit)]
        self.kitty  = []    # [(Value, Suit)]
        self.scores = {}    # team -> num

        self.dealer = random.choice(list(Player))
        self.turn   = (self.dealer % 4) + 1
        self.trumps = None                # Suit
        self.bid    = None                # (num, Suit, team)
        self.phase  = GamePhase.postgame  # GamePhase

    def command(self, cmd):
        cmd.execute(self)

    def bid(self, player, bid):
        if game.phase == GamePhase.bid and game.turn == self.player:
            if self.bid == None:
                self.bid = bid
        else:
            raise IllegalMoveException("bid {} {}".format(player, bid))

    def start(self):
        if self.phase == GamePhase.postgame:
            self._init_deck()
            self.deal()
            self.phase = GamePhase.bid
        else:
            raise IllegalMoveException("start")

    def _init_deck(self):
        """ Initialise the deck to have one joker, the red fours,
            and everything above."""

        self.deck = []

        # Red fours
        self.deck.append((Value.four, Suit.hearts))
        self.deck.append((Value.four, Suit.diamonds))

        # Joker
        self.deck.append((Value.joker, None))

        # Everything else
        for value in map(Value, range(5,15)):
            for suit in map(Suit, range(1,5)):
                self.deck.append((value, suit))

        assert(len(self.deck) == 43)

        # shuffffle
        random.shuffle(self.deck)

    def deal(self):
        for p in Player:
            self.hands[p] = self.deck[:10]
            self.deck = self.deck[10:]

        self.kitty = self.deck 
