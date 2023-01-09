import random
from cards import Deck
from cards import Card
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
        self.hands = [Hand() for i in range(n_players)]

        self.current_index = random.randrange(n_players)
        self.current_hand = self.hands[self.current_index]
        self.current_word = ""
        #self.current_pile = ''

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
        #     output += f"Longer word possible? {self.tr.longer_possible(self.current_word)}\n\n"
        #this is now revealed in the challenge function instead

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
        self.current_word += card.LETTER
        self.deck.current_pile.append(Card(card.LETTER))
        #self.current_hand.add_card(self.deck.draw())
        ## just added to check if regen works

        


    def next_turn(self):
        self.current_index += 1
        if self.current_index >= self.N_PLAYERS:
            self.current_index = 0

        self.current_hand = self.hands[self.current_index]

    def deal(self):
        for i in range(self.N_PLAYERS * 7):
            if len(self.deck.cards) == 0:
               print("Error: You have added too many players for this deck.") 
               return
            self.current_hand.add_card(self.deck.draw())
            self.next_turn()
    
    def challenge(self):
        doubt = input("Challenge this word? ")
        doubt.lower()
        if doubt == 'yes':
            revealer = f"Longer word possible? {self.tr.longer_possible(self.current_word)}\n\n"
            print(revealer)
        return doubt
