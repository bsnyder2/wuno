import sys
import pygame
import data.game
import display.buttons as btns


class GUI():
    def __init__(self):
        # creates a set of valid words from given file
        file = open(sys.path[0] + "/wordsets/words-58k.txt", "r")
        valid_words = {line.strip() for line in file}

        # creates game with wordset valid_words and 4 players
        self.game = data.game.Game(valid_words, 4)

        self.screen = pygame.display.set_mode((500, 500))
        self.background = pygame.Surface((500, 500))
        self.clock = pygame.time.Clock()
        btns.Cursor()
        btns.CompleteButton(self, 420, 220)
        btns.ChallengeButton(self, 420, 280)

        # display all buttons
        self.display_cards()
        btns.Button.button_group.draw(self.screen)
        pygame.display.update()

        self.game_loop()



    
    def display_cards(self):
        print("HERe")
        self.screen.fill((0, 0, 0))
        for card_i, card in enumerate(self.game.current_hand.cards):
            print(card)
            card.card_button = btns.CardButton(self, 40 + card_i * 60, 450, card)
        self.screen.blit(self.background, (0, 0))
        btns.CardButton.card_group.draw(self.screen)
        self.screen.blit(self.background, (0, 0))

        pygame.display.update()

    def game_loop(self):
        while True:
            # update cursor location
            btns.Cursor.cursor_group.update()

            # every frame, check:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # if mouse clicked and button group hit, update and redraw button group
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.groupcollide(btns.Cursor.cursor_group, btns.Button.button_group, False, False):
                    btns.Button.button_group.update()
                    btns.Button.button_group.draw(self.screen)
            
            for card_button in btns.CardButton.card_group:
                if card_button.is_confirmed:
                    self.game.place(card_button.card)
                    self.screen.fill((0, 0, 0))

                    self.display_cards()

                    card_button.is_confirmed = False

            # update display at 60 fps
            pygame.display.update()
            self.clock.tick(60)

def main():
    GUI()

if __name__ == "__main__":
    main()

# def main():
#     # creates a set of valid words from given file
#     file = open(sys.path[0] + "/wordsets/words-58k.txt", "r")
#     valid_words = {line.strip() for line in file}

#     # creates game with wordset valid_words and 4 players
#     game = data.game.Game(valid_words, 4)

#     screen = pygame.display.set_mode((500, 500))
#     clock = pygame.time.Clock()
#     btns.Cursor()

#     # buttons - adds to class group on creation
#     complete_button = btns.CompleteButton(game, 420, 220)
#     challenge_button = btns.ChallengeButton(game, 420, 280)

#     # initial draw buttons
#     btns.Button.button_group.draw(screen)
#     pygame.display.update()

#     while True:
#         # update cursor location
#         btns.Cursor.cursor_group.update()

#         # every frame, check:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#             # if mouse clicked and button group hit, update and redraw button group
#             if event.type == pygame.MOUSEBUTTONDOWN and pygame.sprite.groupcollide(btns.Cursor.cursor_group, btns.Button.button_group, False, False):
#                 btns.Button.button_group.update()
#                 btns.Button.button_group.draw(screen)

#         # update display at 60 fps
#         pygame.display.update()
#         clock.tick(60)


# if __name__ == "__main__":
#     main()
