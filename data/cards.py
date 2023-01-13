import random

LETTER_FREQS = {
    "a": 9,
    "b": 2,
    "c": 2,
    "d": 4,
    "e": 12,
    "f": 2,
    "g": 3,
    "h": 2,
    "i": 9,
    "j": 1,
    "k": 1,
    "l": 4,
    "m": 2,
    "n": 6,
    "o": 8,
    "p": 2,
    "q": 1,
    "r": 6,
    "s": 4,
    "t": 6,
    "u": 4,
    "v": 2,
    "w": 2,
    "x": 1,
    "y": 2,
    "z": 1
}


class Card:
    def __init__(self, letter):
        if letter.lower() not in LETTER_FREQS:
            raise ValueError("Invalid letter assigned to card")
        self.LETTER = letter.lower()

    def __eq__(self, other):
        return self.LETTER == other.LETTER

    def __str__(self):
        return f"[{self.LETTER.upper()}]"


class CardList:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if len(self.cards) < 1:
            return "[empty]"

        output = ""
        for card in self.cards:
            output += str(card) + " "
        return output

    def hidden(self):
        if len(self.cards) < 1:
            return "[empty]"

        output = ""
        for card in self.cards:
            output += "[ ] "
        return output

    def move_all(self, target):
        target.cards.extend(self.cards)
        target.cards.sort(key=lambda c: c.LETTER)
        self.cards.clear()


class Deck(CardList):
    def __init__(self):
        self.cards = []

        # construct deck
        for letter in LETTER_FREQS:
            for i in range(LETTER_FREQS[letter]):
                self.cards.append(Card(letter))

    def draw_to(self, hand):
        hand.cards.append(self.cards.pop(0))
        hand.cards.sort(key=lambda c: c.LETTER)

    def shuffle(self):
        random.shuffle(self.cards)


class Hand(CardList):
    def place(self, center, card):
        if card not in self.cards:
            raise ValueError(f"Card {card} not in hand")
        center.cards.append(card)
        self.cards.remove(card)
