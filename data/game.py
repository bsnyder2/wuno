import random
from cards import Card, CardList, Deck, Hand
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
        self.word_list = CardList()
        self.discard = CardList()
        self.hands = [CardList() for i in range(n_players)]

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
        # output += f"Word valid? {self.current_word in self.VALID_WORDS}\n"

        # can a longer word be made?
        # output += f"Longer word possible? {len(self.tr.continuant_letters(self.current_word)) > 0}\n\n"

        for hand_index, hand in enumerate(self.hands):
            if hand_index == self.current_index:
                output += f"> Player {hand_index}: {hand}\n"
            else:
                output += f"  Player {hand_index}: {hand.hidden()}\n"

        return output

    def prev_hand(self):
        self.prev_index = self.current_index - 1
        if self.prev_index < 0:
            self.prev_index = self.N_PLAYERS - 1
        return self.hands[self.prev_index]

    def challenge_valid(self):
        # current word continuable?
        return not len(self.tr.continuant_letters(self.current_word)) > 0

    def is_complete(self):
        # current word complete?
        return len(self.current_word) > 2 and self.current_word in self.VALID_WORDS

    def draw(self):
        self.current_hand.add_card(self.deck.draw())

    def place(self, card):
        if card not in self.current_hand:
            raise ValueError(f"Card {card} not in hand")
        self.current_hand.remove_card(card)
        self.word_list.add_card(card)
        self.current_word += card.LETTER
        self.deck.current_pile.append(Card(card.LETTER))

    def next_player(self):
        self.current_index += 1
        if self.current_index >= self.N_PLAYERS:
            self.current_index = 0

        self.current_hand = self.hands[self.current_index]

    def deal(self):
        for i in range(self.N_PLAYERS * 3):
            self.current_hand.add_card(self.deck.draw())
            self.next_player()


    def move_card(self, origin, target, card):
        origin.cards.remove(card)
        target.cards.add(card)
        target.cards.sort(key=lambda c: c.LETTER)

    def move_all(self,origin,target):
        target.cards.extend(origin.cards)
        origin.cards.clear()
        target.cards.sort(key=lambda c: c.LETTER)
        



    # def add_card(self, card):
    #     # adds card to hand and sorts alphabetically
    #     self.cards.append(card)
    #     self.cards.sort(key=lambda c: c.LETTER)

    # def add_from(self, list):
    #     self.cards.extend(list.cards)
    #     list.cards = []
    #     self.cards.sort(key=lambda c: c.LETTER)

    # def remove_card(self, card):
    #     self.cards.remove(card)