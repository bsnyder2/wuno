import math
import sys
import pygame
import data.game
import display.buttons as btns
import math

pygame.init()

# prints equivalent text info to gui
debug = True


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
        # creates a set of valid words from given file
        file = open(sys.path[0] + "/wordsets/words-58k.txt", "r")
        valid_words = {line.strip() for line in file}

        # creates game with wordset valid_words and 4 players
        self.game = data.game.Game(valid_words, 4)

        # pygame setup
        self.screen = pygame.display.set_mode((1300, 800))
        self.clock = pygame.time.Clock()

        # initialize cursor and buttons
        btns.Cursor()
        btns.ActionButton(420, 220, "Complete")
        btns.ActionButton(420, 280, "Challenge")

        if self.game.N_PLAYERS >= 2:
            DisplayHand(0)
            DisplayHand(2)
        if self.game.N_PLAYERS >= 3:
            DisplayHand(1)
        if self.game.N_PLAYERS == 4:
            DisplayHand(3)

        # display all buttons
        self.refresh_cards()
        self.game_loop()

    def refresh_cards(self):
        # kill all buttons
        for button in btns.CardButton.button_group:
            pygame.sprite.Sprite.kill(button)

        # clear screen
        self.screen.fill((0, 0, 0))

        # assign buttons to cards in current hand
        for hand_i, hand in enumerate(self.game.hands):
            coords = self.polar_to_cart(
                (100, 3 * math.pi / 2 + hand_i * math.pi / 2))
            pygame.Surface.set_at(self.screen, coords, (255, 255, 255))

        for card_i, card in enumerate(self.game.current_hand.cards):
            card.card_button = btns.CardButton(card, 40 + card_i * 60, 450)

        # redraw buttons
        btns.Button.button_group.draw(self.screen)

        if debug:
            print("\nCurrent word:", self.game.current_word)
            print("Center:", self.game.center)
            print("Current hand:", self.game.current_hand)
            print(f"Discard pile: {self.game.discard}\n")

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

            # for all buttons:
            for button in btns.Button.button_group:
                # if confirmed card, place and refresh
                if button.is_confirmed:
                    if debug:
                        print("CONFIRMED", button.card)
                    self.game.place(button.card)
                    self.refresh_cards()
                    button.is_confirmed = False
                # if pressed action button, do corresponding action and refresh
                elif button.is_pressed:
                    if button.word == "Complete":
                        self.game.run_complete()
                    else:
                        self.game.run_challenge()
                    self.refresh_cards()
                    button.is_pressed = False

            # update display at 60 fps
            pygame.display.update()
            self.clock.tick(60)

    def polar_to_cart(self, point):
        # centered at (250, 250)
        r, theta = point
        x = int(r * math.cos(theta)) + 250
        y = int(r * math.sin(theta)) + 250
        return x, y
