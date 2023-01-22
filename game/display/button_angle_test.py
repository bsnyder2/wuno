import math
import sys
import pygame
import data.cards
import display.buttons as btns

pygame.init()


class DisplayHand():
    def __init__(self, loc):
        theta = (math.pi / 2) + (2 * loc * math.pi / 4)
        hand_center = self.polar_to_cart((200, theta))

        btns.CardButton(data.cards.Card("A"), 50, 50)

        for card_i in range(5):
            # initialize card with default center (since rect needs to be reset)
            card_button = btns.CardButton(data.cards.Card("q"))

            # recreate image, rotated accordingly
            card_button.image = pygame.transform.rotate(
                card_button.image, 90 - 180 * theta / math.pi)
            card_button.rect = card_button.image.get_rect()

            card_button.rect.center = (
                hand_center[0] + 10, hand_center[1] + card_i * 20)

    def polar_to_cart(self, point):
        # centered at (250, 250)
        r, theta = point
        x = round(r * math.cos(theta)) + 250
        y = round(r * math.sin(theta)) + 250
        return x, y


class GUI():
    def __init__(self):
        self.n_hands = 3

        # pygame setup
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()

        # display hands in locations depending on n
        if self.n_hands >= 2:
            DisplayHand(0)
            DisplayHand(2)
        if self.n_hands >= 3:
            DisplayHand(1)
        if self.n_hands == 4:
            DisplayHand(3)

        # display all buttons
        btns.Button.button_group.draw(self.screen)
        self.game_loop()

    def game_loop(self):
        while True:
            # update cursor location
            btns.Cursor.cursor_group.update()

            # every frame, check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if mouse clicked and button group hit, update and redraw button group (for selection)
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.groupcollide(btns.Cursor.cursor_group, btns.Button.button_group, False, False):
                    btns.Button.button_group.update()
                    btns.Button.button_group.draw(self.screen)

            # update display at 60 fps
            pygame.display.update()
            self.clock.tick(60)
