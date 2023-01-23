import sys
import data.game
import data.server
import display.gui

def main():
    HOST_IP = "10.17.50.224"
    PORT = 50000

    file = open(sys.path[0] + "/assets/wordsets/words-58k.txt", "r")
    valid_words = {line.strip() for line in file}

    # creates game with wordset valid_words and n players
    game = data.game.Game(valid_words, 4)

    # start server
    sv = data.server.Server(HOST_IP, PORT)
    sv.start()


if __name__ == "__main__":
    main()