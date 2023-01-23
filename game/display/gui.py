import math
import sys
import pygame
import data.game
import display.sprites as sprites

pygame.init()

# prints equivalent text info to gui
debug = True


class DisplayHand:
    def __init__(self, hand, position):
        self.hand = hand
        self.position = position
        self.theta = (math.pi / 2) + (2 * position * math.pi / 4)
        self.hand_center = self.polar_to_cart((200, self.theta))

    def assign_buttons(self, is_current):
        for card_i, card in enumerate(self.hand.cards):
            # initialize CardButton with default center (since rect needs to be reset)
            # hidden if not current hand
            card.card_button = sprites.CardButton(card, not is_current)
            # rotate image
            card.card_button.image = pygame.transform.rotate(
                card.card_button.image, 90 - 180 * self.theta / math.pi)
            # set rect dimensions to image
            card.card_button.rect = card.card_button.image.get_rect()

            # compress cards if too many
            inter_dist = 60
            if len(self.hand.cards) > 5:
                inter_dist = 240 / (len(self.hand.cards) - 1)

            # set card centers accordingly
            offset = (len(self.hand.cards) - 1) * inter_dist / 2
            if self.position > 1:
                card_i = -card_i
                offset = -offset
            if self.position % 2 == 0:
                card.card_button.rect.center = (
                    self.hand_center[0] + card_i * inter_dist - offset, self.hand_center[1])
            else:
                card.card_button.rect.center = (
                    self.hand_center[0], self.hand_center[1] + card_i * inter_dist - offset)

    def polar_to_cart(self, point):
        # centered at (250, 250)
        r, theta = point
        x = round(r * math.cos(theta)) + 250
        y = round(r * math.sin(theta)) + 250
        return x, y


class DisplayCenter:
    def __init__(self, center):
        self.center = center

    def assign_buttons(self):
        for card_i, card in enumerate(self.center.cards):
            inter_dist = 60
            offset = (len(self.center.cards) - 1) * inter_dist / 2

            card.card_button = sprites.CardButton(
                card, False, 250 + card_i * inter_dist - offset, 190)
            card.card_button.is_active = False


class GUI:
    def __init__(self, game):
        self.game = game

        # pygame setup
        self.screen = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()

        # initialize cursor and buttons
        sprites.Cursor()
        sprites.ActionButton("COMPLETE", 310, 280)
        sprites.ActionButton("CHALLENGE", 310, 340)
        sprites.DeckButton(190, 310)

        self.display_hands = []
        # 2 players: across
        if self.game.N_PLAYERS == 2:
            self.display_hands.append(DisplayHand(self.game.hands[0], 0))
            self.display_hands.append(DisplayHand(self.game.hands[1], 2))
        # 3 or 4 players: all spots
        elif self.game.N_PLAYERS >= 3:
            self.display_hands.append(DisplayHand(self.game.hands[0], 0))
            self.display_hands.append(DisplayHand(self.game.hands[1], 1))
            self.display_hands.append(DisplayHand(self.game.hands[2], 2))
        if self.game.N_PLAYERS == 4:
            self.display_hands.append(DisplayHand(self.game.hands[3], 3))

        self.display_center = DisplayCenter(self.game.center)
        # print(self.display_center.center.cards[0])

        # display all buttons
        self.refresh_cards()
        self.game_loop()

    def refresh_cards(self):
        # kill all CardButtons
        for card in sprites.CardButton.card_group:
            pygame.sprite.Sprite.kill(card)

        # clear screen
        self.screen.fill((0, 0, 0))

        # assign buttons to cards in current hand
        for display_hand in self.display_hands:
            is_current = display_hand.hand == self.game.current_hand
            display_hand.assign_buttons(is_current)
        self.display_center.assign_buttons()

        # redraw buttons
        sprites.Button.button_group.draw(self.screen)

        if debug:
            if self.game.current_word == "":
                print("\nCurrent word: [empty]")
            else:
                print("\nCurrent word:", self.game.current_word.upper())
            print("Center:", self.game.center)
            print("Current hand:", self.game.current_hand)
            print(f"Discard pile: {self.game.discard}\n")

    def game_loop(self):
        while True:
            # update cursor location
            sprites.Cursor.cursor_group.update()

            # every frame, check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if mouse clicked and button group hit, update and redraw button group (for selection)
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.groupcollide(sprites.Cursor.cursor_group, sprites.Button.button_group, False, False):
                    sprites.Button.button_group.update()
                    sprites.Button.button_group.draw(self.screen)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.game.card_placed == True:
                            self.game.hand_forward()
                            self.refresh_cards()
                            self.game.card_placed = False

            # for all buttons:
            for button in sprites.Button.button_group:
                # if confirmed card, place and refresh
                if button.is_confirmed and self.game.card_placed == False:
                    if debug:
                        print("CONFIRMED", button.card)
                    self.game.place(button.card)
                    self.refresh_cards()
                    button.is_confirmed = False
                # if pressed action button, do corresponding action and refresh
                elif button.is_pressed:
                    if isinstance(button, sprites.DeckButton):
                        if debug:
                            print("DREW CARD")
                        self.game.draw_n(self.game.current_hand, 1)
                    elif button.WORD == "COMPLETE":
                        self.game.run_complete()
                    elif self.game.card_placed == False:
                        self.game.run_challenge()
                    self.refresh_cards()
                    button.is_pressed = False

            # update display at 60 fps
            pygame.display.update()
            self.clock.tick(60)
