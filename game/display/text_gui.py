import sys
import data.game


def main():
    # creates a set of valid words from given file
    file = open(sys.path[0] + "/wordsets/words-58k.txt", "r")
    valid_words = {line.strip() for line in file}

    # creates game with wordset valid_words and 4 players
    g = data.game.Game(valid_words, 4)

    while True:
        print(g)
        g.run_turn()


if __name__ == "__main__":
    main()
