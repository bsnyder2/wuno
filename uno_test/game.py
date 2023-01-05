import random
from cards import Deck
from hand import Hand

class Game:
    def __init__(self, valid_words, n_players):
        self.valid_words = valid_words
        self.n_players = n_players

        self.deck = Deck()
        self.hands = [Hand() for i in range(n_players)]
        self.current_index = random.randrange(n_players)
        self.current_hand = self.hands[self.current_index]
        self.current_word = ""

        self.deck.shuffle()
        self.__deal()

    def __str__(self):
        output = ""

        if len(self.current_word) < 1:
            output += "Current word: [empty]\n"
        else:
            output += f"Current word: {self.current_word.upper()}\n"

        # isComplete
        output += f"Word valid? {self.current_word in self.valid_words}\n\n"

        for hand_index, hand in enumerate(self.hands):
            if hand_index == self.current_index:
                output += "> "
            else:
                output += "  "
            output += f"Player {hand_index}: {hand}\n"

        return output

    def place(self, card):
        if card not in self.current_hand:
            raise ValueError(f"Card {card} not in hand")
        self.current_hand.remove_card(card)
        self.current_word += card.get_letter()

    def next_turn(self):
        self.current_index += 1
        if self.current_index >= self.n_players:
            self.current_index = 0

        self.current_hand = self.hands[self.current_index]

    def __deal(self):
        for i in range(self.n_players * 7):
            self.current_hand.add_card(self.deck.draw())
            self.next_turn()

    def __is_longer_possible(self):
        pass