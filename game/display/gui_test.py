import sys
import pygame
import data.game
import display.buttons as btns
import math

pygame.init()

# prints equivalent text info to gui
debug = True


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

        # display all buttons
        self.refresh_cards()
        self.game_loop()

    def refresh_cards(self):
        # kill all card sprites
        for card_button in btns.CardButton.card_group:
            pygame.sprite.Sprite.kill(card_button)

        # clear screen
        self.screen.fill((0, 0, 0))

        # assign buttons to cards in current hand
        for hand_i in range(len(self.game.hands)):
            for card_i, card in enumerate(self.game.hands[hand_i].cards):
                card.card_button = btns.CardButton(650 - 125 / 2 + (len(self.game.current_hand.cards) - 2 * card_i) * 62.5,
                800 * (((hand_i // 2) + 1) % 2) - 175 / 2 + 175  *(((hand_i // 2) + 2) % 2),
                card)
                # surf_center = (
                #     (-40 - 10 * abs(- card_i + (len(hand_i) - 1) / 2) ** 1.7),
                #     ((SCREEN_HEIGHT / 2 - card.image.get_height()) / 2 + (hands[2] - 1 - i) * 87.5)
                # )
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
