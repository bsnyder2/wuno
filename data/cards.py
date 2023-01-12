import random

# taken directly from scrabble - associates letters with frequencies
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

    def __contains__(self, card):
        return card in self.cards

    def __str__(self):
        output = ""

        if len(self.cards) < 1:
            return "[empty]"
        for card in self.cards:
            output += str(card) + " "

        return output

    def hidden(self):
        output = ""

        if len(self.cards) < 1:
            return "[empty]"
        for card in self.cards:
            output += "[ ] "

        return output

    def letters(self):
        return set([card.LETTER for card in self.cards])

    def add_card(self, card):
        # adds card to hand and sorts alphabetically
        self.cards.append(card)
        self.cards.sort(key=lambda c: c.LETTER)

    def add_from(self, list):
        self.cards.extend(list.cards)
        list.cards = []
        self.cards.sort(key=lambda c: c.LETTER)


class Deck(CardList):
    def __init__(self):
        self.cards = []
        self.current_pile = []

        # build deck
        for letter in LETTER_FREQS:
            for i in range(LETTER_FREQS[letter]):
                self.cards.append(Card(letter))

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


class Hand(CardList):
    def remove_card(self, card):
        self.cards.remove(card)

    # TODO change remove_card and add_card to one move_card method
