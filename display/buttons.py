import sys
import pygame


class Cursor(pygame.sprite.Sprite):
    # invisible mouse sprite class: there is only one of these objects for the whole game --> functions as our "clicker"

    def __init__(self):
        super().__init__()
        # cursor hitbox
        self.rect = pygame.Rect(0, 0, 1, 1)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def check_hits(self, button_group):
        for button in button_group:
            if pygame.sprite.collide_rect(self, button):
                button.update()


class Button(pygame.sprite.Sprite):
    # Button Superclass: this is what specific buttons should inherit from

    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.color = (255, 255, 255)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    # on click
    def update(self):
        if self.color == (255, 255, 255):
            self.color = (255, 0, 0)
        else:
            self.color = (255, 255, 255)
        self.image.fill(self.color)
        # replace/add on specific response depending on what you want your button to do


class SusanneButton(Button):
    # Example Button Subclass

    def __init__(self, width, height, pos_x, pos_y):
        super().__init__(width, height, pos_x, pos_y)

    def update(self):
        if self.color == (255, 255, 255):
            self.color = (0, 255, 0)
        else:
            self.color = (255, 255, 255)
        self.image.fill(self.color)


class CardButton(Button):
    # CardButton should be attribute of Card?

    def __init__(self, pos_x, pos_y):
        super().__init__(50, 70, pos_x, pos_y)


def main():
    pygame.init()
    clock = pygame.time.Clock()

    # Set up the drawing window
    screen = pygame.display.set_mode([500, 500])

    # invisible mouse sprite group
    cursor_group = pygame.sprite.GroupSingle(Cursor())

    # buttons
    challenge_button = Button(50, 50, 100, 100)
    susanne_button = SusanneButton(60, 30, 200, 200)
    card_button = CardButton(300, 300)

    button_group = pygame.sprite.Group()
    button_group.add(challenge_button)
    button_group.add(susanne_button)
    button_group.add(card_button)

    # initial draw buttons
    button_group.draw(screen)

    # True loop not necessary for final module, should be combined w GUI loop later on
    while True:
        # update cursor location
        cursor_group.update()

        # every frame, check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if mouse clicked, update buttons if hit and redraw
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_group.sprite.check_hits(button_group)
                button_group.draw(screen)

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
