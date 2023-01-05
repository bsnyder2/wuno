import random
import sys
# import pygame

# taken directly from scrabble
LETTER_VALUES = {
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
}


class Card:
    def __init__(self, letter):
        if not isinstance(letter, str):
            raise TypeError("Invalid value assigned to card")

        std_letter = letter.lower()
        if std_letter not in LETTER_VALUES:
            raise ValueError("Invalid letter assigned to card")

        self.letter = std_letter
        self.value = LETTER_VALUES[std_letter]

    def __str__(self):
        return f"[{self.letter.upper()}]"

    def get_letter(self):
        return self.letter

    def get_value(self):
        return self.value


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        output = ""
        for card in self.cards:
            output += str(card) + " "

        return output

    def add_card(self, card):
        if not isinstance(card, Card):
            raise TypeError("Invalid object added to hand")

        # adds card to hand and sorts alphabetically
        self.cards.append(card)
        self.cards.sort(key=Card.get_letter)


class Game:
    def __init__(self, valid_words, n_players):
        self.valid_words = valid_words
        self.n_players = n_players


        self.hands = [Hand() for i in range(n_players)]
        self.current_index = random.randrange(n_players)
        self.current_hand = self.hands[self.current_index]
        self.current_word = ""


    def __str__(self):
        output = ""

        if len(self.current_word) < 1:
            output += "Current word: [empty]\n"
        else:
            output += f"Current word: {self.current_word.upper()}\n"

        # isComplete
        output += str(self.current_word in self.valid_words) + "\n"


        for hand_index, hand in enumerate(self.hands):
            if hand_index == self.current_index:
                output += "> "
            else:
                output += "  "
            output += f"Player {hand_index}: {hand}\n"

        return output

    def place(self, card):
        # self.current_hand.remove(card)
        self.current_word += card.get_letter()

    def get_current_hand(self):
        return self.current_hand

    def next_turn(self):
        self.current_index += 1
        if self.current_index >= self.n_players:
            self.current_index = 0

        self.current_hand = self.hands[self.current_index]

    def print_turn(self):
        print(f"Player {self.current_index}'s turn:\n{self.current_hand}")


def main():
    # creates a set of valid words from given file
    file = open(sys.path[0] + "/wordsets/words-58k.txt", "r")
    valid_words = {line.strip() for line in file}

    g = Game(valid_words, 4)

    g.get_current_hand().add_card(Card("a"))

    for i in range(5):
        g.place(Card("j"))
        print(g)
        g.next_turn()


    # print(words)


if __name__ == "__main__":
    main()


# ideas
# uno like game

# go around in a circle, everyone has cards with letters on them as well as special cards
# cards have letters, also colors that have different properties?
# put down a card to add it to the word
# look at list of words and see if any words start with the given letters on the table - if not, penalize the person who put down the last card
# number of each letter and point values are like scrabble rules
# longer words, and words that use rarer letters, get more points
# anyone can decide to end the word with a letter if they want (maybe have a special end card? or always give the option)
# whoever finishes the word gets the points
