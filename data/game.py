import random
from cards import CardList, Deck, Hand
from word_trie import WordTrie
from text_input import TextInput


class Game:
    def __init__(self, valid_words, n_players):
        # constants
        self.VALID_WORDS = valid_words
        self.N_PLAYERS = n_players
        self.tr = WordTrie()
        for word in self.VALID_WORDS:
            self.tr.insert(word)

        # CardLists
        self.deck = Deck()
        self.center = CardList()
        self.discard = CardList()
        self.hands = [Hand() for i in range(n_players)]

        # game status
        self.current_index = random.randrange(n_players)
        self.current_hand = self.hands[self.current_index]
        self.current_word = ""

        # initial shuffle
        self.deck.shuffle()

        # deal cards
        for i in range(n_players):
            self.draw_n(self.current_hand, 5)
            self.hand_forward()

    def __str__(self):
        output = ""

        if len(self.current_word) < 1:
            output += "Current word: [empty]\n"
        else:
            output += f"Current word: {self.current_word.upper()}\n"

        output += f"Word complete? {self.is_current_complete()}\n"
        output += f"Word continuable? {self.is_current_continuable()}\n\n"

        for hand_index, hand in enumerate(self.hands):
            if hand_index == self.current_index:
                output += f"> Player {hand_index}: {hand}\n"
            else:
                output += f"  Player {hand_index}: {hand.hidden()}\n"

        return output

    def run_turn(self):
        # 1. challenge that current word is complete
        if TextInput("Challenge complete?").get_bool():
            if self.is_current_complete():
                print("Challenge successful")
                self.draw_n(self.prev_hand(), 2)
            else:
                print("Challenge failed")
                self.draw_n(self.current_hand, 2)
            return

        # 2. challenge that current word is not continuable
        if TextInput("Challenge continuable?").get_bool():
            if not self.is_current_continuable():
                print("Challenge successful")
                self.center.move_all(self.prev_hand())
            else:
                print("Challenge failed")
                self.center.move_all(self.current_hand)
            return

        # 3. draw card(s)
        while TextInput("Draw card?").get_bool():
            self.draw_n(self.current_hand, 1)

        # 4. place card
        pl_card = TextInput("Place card").get_card()
        self.current_hand.place(self.center, pl_card)
        self.current_word += pl_card.LETTER
        print(self)

        # 5. claim that current word is complete
        if TextInput("Claim complete?").get_bool():
            if self.is_current_complete():
                self.center.move_all(self.discard)
                self.current_word = ""
            else:
                self.draw_n(self.current_hand, 2)

        self.hand_forward()

    def is_current_complete(self):
        return len(self.current_word) > 2 and self.current_word in self.VALID_WORDS

    def is_current_continuable(self):
        return len(self.tr.continuant_letters(self.current_word)) > 0

    def draw_n(self, hand, n):
        for i in range(n):
            self.deck.draw_to(hand)

    def prev_hand(self):
        prev_index = self.current_index - 1
        if prev_index < 0:
            prev_index = self.N_PLAYERS - 1
        return self.hands[prev_index]

    def hand_forward(self):
        self.current_index += 1
        if self.current_index > self.N_PLAYERS - 1:
            self.current_index = 0
        self.current_hand = self.hands[self.current_index]
