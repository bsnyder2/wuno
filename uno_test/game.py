import random
from cards import Deck
from discard import Discard
from hand import Hand
from word_trie import WordTrie


class Game:
    def __init__(self, valid_words, n_players):
        # constants (word trie will not change after loaded)
        self.VALID_WORDS = valid_words
        self.N_PLAYERS = n_players
        self.tr = WordTrie()
        for word in self.VALID_WORDS:
            self.tr.insert(word)

        self.deck = Deck()
        self.discard = Discard()
        self.hands = [Hand() for i in range(n_players)]

        self.current_index = random.randrange(n_players)
        self.current_hand = self.hands[self.current_index]
        self.current_word = ""

        self.deck.shuffle()
        self.deal()

    def __str__(self):
        output = ""

        if len(self.current_word) < 1:
            output += "Current word: [empty]\n"
        else:
            output += f"Current word: {self.current_word.upper()}\n"

        # is the current word valid?
        output += f"Word valid? {self.current_word in self.VALID_WORDS}\n"

        # can a longer word be made?
        output += f"Continuable? {len(self.tr.continuant_letters(self.current_word)) > 0}\n"

        # can the current word be continued by the current player's hand?
        # does current player's hand contain at least one of current node's children?
        output += f"Continuable by current? {len(self.tr.continuant_letters(self.current_word).intersection(self.current_hand.letters())) > 0}\n\n"

        for hand_index, hand in enumerate(self.hands):
            if hand_index == self.current_index:
                output += "> "
            else:
                output += "  "
            output += f"Player {hand_index}: {hand}\n"

        return output

    def prev_hand(self):
        self.prev_index = self.current_index - 1
        if self.prev_index < 0:
            self.prev_index = self.N_PLAYERS
        return self.hands[self.prev_index]

    def challenge(self):
        # current word continuable?
        return not len(self.tr.continuant_letters(self.current_word)) > 0

    def draw(self):
        self.current_hand.add_card(self.deck.draw())

    # def draw_until(self):
    #     # put this in a variable bc will stay the same as cards are drawn
    #     continuant_letters = self.tr.continuant_letters(self.current_word)

    #     # if the current word can be continued by some letter
    #     if len(continuant_letters) > 0:
    #         # while the current hand has no cards to continue the word, draw
    #         while len(continuant_letters.intersection(self.current_hand.letters())) < 1:
    #             self.current_hand.add_card(self.deck.draw())

    def place(self, card):
        if card not in self.current_hand:
            raise ValueError(f"Card {card} not in hand")
        self.current_hand.remove_card(card)
        self.discard.add_card(card)
        self.current_word += card.LETTER

    def next_player(self):
        self.current_index += 1
        if self.current_index >= self.N_PLAYERS:
            self.current_index = 0

        self.current_hand = self.hands[self.current_index]

    def deal(self):
        for i in range(self.N_PLAYERS * 3):
            self.current_hand.add_card(self.deck.draw())
            self.next_player()
