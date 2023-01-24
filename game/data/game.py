import data.cards
import data.word_trie


class Game:
    def __init__(self, valid_words, n_players):
        # constants
        self.VALID_WORDS = valid_words
        self.N_PLAYERS = n_players
        self.tr = data.word_trie.WordTrie()
        for word in self.VALID_WORDS:
            self.tr.insert(word)

        # CardLists
        self.deck = data.cards.Deck()
        self.center = data.cards.CardList()
        self.discard = data.cards.CardList()
        self.hands = [data.cards.Hand() for i in range(n_players)]

        # game status
        self.current_index = 0
        self.current_hand = self.hands[self.current_index]
        self.current_word = ""
        self.is_card_placed = False

        # initial shuffle
        self.deck.shuffle()

        # deal cards
        for i in range(n_players):
            self.draw_n(self.current_hand, 5)
            self.hand_forward()

    def place(self, pl_card):
        self.current_hand.place(self.center, pl_card)
        self.current_word += pl_card.LETTER
        self.is_card_placed = True

    def run_complete(self):
        if len(self.current_word) > 2 and self.current_word in self.VALID_WORDS:
            # reset center word
            self.center.move_all(self.discard)
            self.current_word = ""
            if not self.is_card_placed:
                self.draw_n(self.prev_hand(), 2)
                # called previous player successfully
                return 1
            # completed word on own turn
            return 0
        else:
            # called previous player unsuccessfully
            self.draw_n(self.current_hand, 2)
            return 2

    def run_challenge(self):
        if len(self.tr.continuant_letters(self.current_word)) < 1:
            self.center.move_all(self.prev_hand())
            self.current_word = ""
            return True
        else:
            if len(self.current_hand.cards) < 1:
                print("Player", self.current_index + 1, "has won the game!")
                exit(0)
            self.center.move_all(self.current_hand)
            self.current_word = ""
            return False

    def draw_n(self, hand, n):
        for i in range(n):
            if len(self.deck.cards) < 1:
                self.deck.regen(self.discard)
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
        self.is_card_placed = False
