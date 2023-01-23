import data.cards
import data.word_trie


class Game:
    def __init__(self, valid_words, n_players):
        # constants
        self.VALID_WORDS = valid_words
        self.N_PLAYERS = n_players
        self.tr = data.word_trie.WordTrie()
        self.card_placed = False
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

        # initial shuffle
        self.deck.shuffle()

        # deal cards
        for i in range(n_players):
            self.draw_n(self.current_hand, 5)
            self.hand_forward()

    def place(self, pl_card):
        self.current_hand.place(self.center, pl_card)
        self.current_word += pl_card.LETTER
        self.card_placed = True

    def run_complete(self):
        if len(self.current_word) > 2 and self.current_word in self.VALID_WORDS:
            print("Word is complete: previous player draws 2")
            self.draw_n(self.prev_hand(), 2)
            # reset center word
            self.center.move_all(self.discard)
            self.current_word = ""
        else:
            print("Word is incomplete: current player draws 2")
            self.draw_n(self.current_hand, 2)
        self.hand_forward()

    def run_challenge(self):
        if len(self.tr.continuant_letters(self.current_word)) < 1:
            print("Word is not continuable: previous player takes center")
            self.center.move_all(self.prev_hand())
        else:
            print("Word is continuable: current player takes center")
            self.center.move_all(self.current_hand)
        self.current_word = ""
        self.hand_forward()

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
        self.card_placed = False
