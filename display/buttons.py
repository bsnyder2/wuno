import sys
import pygame

pygame.init()


class Cursor(pygame.sprite.Sprite):
    # invisible mouse sprite class: there is only one of these objects for the whole game --> functions as our "clicker"

    def __init__(self):
        super().__init__()
        # cursor hitbox
        self.rect = pygame.Rect(0, 0, 1, 1)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Button(pygame.sprite.Sprite):
    # Button Superclass: this is what specific buttons should inherit from

    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        # common scaled font for all buttons
        self.font = pygame.font.SysFont(None, width)

        # image
        self.image = pygame.Surface((width, height))
        self.color = (255, 255, 255)
        self.image.fill(self.color)

        # rect
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

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

    def __init__(self, pos_x, pos_y, letter):
        super().__init__(50, 70, pos_x, pos_y)
        self.is_selected = False

        # letter
        self.text = self.font.render(letter.upper(), False, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.image.blit(
            self.text, (25 - self.text_w / 2, 35 - self.text_h / 2))

    def select(self):
        self.image.fill((0, 255, 0))
        self.image.blit(
            self.text, (25 - self.text_w / 2, 35 - self.text_h / 2))
        self.is_selected = True

    def deselect(self):
        self.image.fill(self.color)
        self.image.blit(
            self.text, (25 - self.text_w / 2, 35 - self.text_h / 2))
        self.is_selected = False

    def update(self, card_group):
        if self.is_selected:
            self.deselect()
        else:
            for card in card_group:
                card.deselect()
            self.select()


def main():
    clock = pygame.time.Clock()

    # Set up the drawing window
    screen = pygame.display.set_mode((500, 500))

    # invisible mouse sprite group
    cursor_group = pygame.sprite.GroupSingle(Cursor())

    # buttons
    challenge_button = Button(50, 50, 100, 100)
    susanne_button = SusanneButton(60, 30, 200, 200)
    c1 = CardButton(300, 300, "a")
    c2 = CardButton(370, 350, "e")
    c3 = CardButton(100, 200, "J")

    button_group = pygame.sprite.Group()
    button_group.add(challenge_button)
    button_group.add(susanne_button)
    button_group.add(c1, c2, c3)
    
    card_group = pygame.sprite.Group(c1, c2, c3)

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
                for card in card_group:
                    if pygame.sprite.collide_rect(cursor_group.sprite, card):
                        card.update(card_group)
                        
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
