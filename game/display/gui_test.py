import sys
import pygame
import data.game
from display.buttons import Cursor, Button, CardButton


def main():
    # creates a set of valid words from given file
    file = open(sys.path[0] + "wordsets/words-58k.txt", "r")
    valid_words = {line.strip() for line in file}

    # creates game with wordset valid_words and 4 players
    g = data.game.Game(valid_words, 4)

    while True:
        print(g)
        g.run_turn()


def main():
    clock = pygame.time.Clock()

    # Set up the drawing window
    screen = pygame.display.set_mode((500, 500))

    # invisible mouse sprite group
    Cursor()

    # buttons - adds to class group on creation
    Button(50, 50, 100, 100)
    CardButton(300, 300, "a")
    CardButton(370, 350, "e")
    CardButton(100, 200, "J")

    # initial draw buttons
    Button.button_group.draw(screen)

    # True loop not necessary for final module, should be combined w GUI loop later on
    while True:
        # update cursor location
        Cursor.cursor_group.update()

        # every frame, check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if mouse clicked and button group hit, update and redraw button group
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.groupcollide(Cursor.cursor_group, Button.button_group, False, False):
                Button.button_group.update()
                Button.button_group.draw(screen)

        # update display at 60 fps
        pygame.display.update()
        clock.tick(60)


# TODO
# make a card subclass of button
    # def show_card(self):
    #     pass
    #     #gets called when you press a card in your hand
    #     #move card up and magnify it
# make challenge button --> maybe 2? one for complete, one for continuable?


if __name__ == "__main__":
    main()