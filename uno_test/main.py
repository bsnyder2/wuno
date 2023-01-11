import sys
from cards import Card
from game import Game
import time

def main():
    # creates a set of valid words from given file
    file = open(sys.path[0] + "/../wordsets/words-58k.txt", "r")
    valid_words = {line.strip() for line in file}

    # creates game with wordset valid_words and 4 players
    g = Game(valid_words, 4)
    
    while True:
        print(g)
        if g.challenge() == 'yes':
            time.sleep(1.5)  
        else:
            g.place(Card(input("Enter card: ")))
        g.next_turn()
        

    print(g)


if __name__ == "__main__":
    main()


# ideas
# uno like game

# go around in a circle, everyone has cards with letters on them as well as special cards
# cards have letters, also colors that have different properties?
# put down a card to add it to the word - done
# look at list of words and see if any words start with the given letters on the table - if not, penalize the person who put down the last card
# number of each letter and point values are like scrabble rules
# longer words, and words that use rarer letters, get more points
# anyone can decide to end the word with a letter if they want (maybe have a special end card? or always give the option)
# whoever finishes the word gets the points


# or ghost
# you can put down a letter, other person can challenge that no word can be completed from given letters
