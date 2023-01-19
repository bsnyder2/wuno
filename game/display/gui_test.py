import sys
import pygame
from display.buttons import Cursor, Button, CardButton


class GUI:
    def __init__(self, game):
        self.game = game


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


if __name__ == "__main__":
    main()
