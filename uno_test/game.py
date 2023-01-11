import random
from cards import Card, Deck
from played_lists import Discard, WordList
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
        self.word_list = WordList()
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
