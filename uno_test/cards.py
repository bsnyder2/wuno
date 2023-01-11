import random
from card_list import CardList

# taken directly from scrabble - associates letters with values and frequencies
LETTER_VALUES_FREQS = {
    "a": (1, 9),
    "b": (3, 2),
    "c": (3, 2),
    "d": (2, 4),
    "e": (1, 12),
    "f": (4, 2),
    "g": (2, 3),
    "h": (4, 2),
    "i": (1, 9),
    "j": (8, 1),
    "k": (5, 1),
    "l": (1, 4),
    "m": (3, 2),
    "n": (1, 6),
    "o": (1, 8),
    "p": (3, 2),
    "q": (10, 1),
    "r": (1, 6),
    "s": (1, 4),
    "t": (1, 6),
    "u": (1, 4),
    "v": (4, 2),
    "w": (4, 2),
    "x": (8, 1),
    "y": (4, 2),
    "z": (10, 1)
}


class Card:
    def __init__(self, letter):
        if not isinstance(letter, str):
            raise TypeError("Invalid value assigned to card")

        std_letter = letter.lower()
        if std_letter not in LETTER_VALUES_FREQS:
            raise ValueError("Invalid letter assigned to card")

        self.LETTER = std_letter
        self.VALUE = LETTER_VALUES_FREQS[std_letter][0]

    def __eq__(self, other):
        return self.LETTER == other.LETTER

    def __str__(self):
        return f"[{self.LETTER.upper()}]"


class Deck(CardList):
    def __init__(self):
        self.cards = []
        self.current_pile = []

        # build deck
        for letter in LETTER_VALUES_FREQS:
            for i in range(LETTER_VALUES_FREQS[letter][1]):
                self.cards.append(Card(letter))

        #self.deck_copy = self.cards.copy()

    def draw(self):
        if len(self.cards) == 0:
            self.regen()
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)


    def regen(self):
        self.cards.extend(self.current_pile)
        self.shuffle()
        # print(self.cards)
        # note: this basically gives you a brand-new shuffled deck,
        #  meaning that if ppl have cards in their hands,
        # there will be more total cards than in a single deck
