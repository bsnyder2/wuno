import sys
import pygame

pygame.init()


class Cursor(pygame.sprite.Sprite):
    # invisible mouse sprite class: there is only one of these objects for the whole game --> functions as our "clicker"
    cursor_group = pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        # cursor hitbox
        self.rect = pygame.Rect(0, 0, 1, 1)
        Cursor.cursor_group.add(self)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Button(pygame.sprite.Sprite):
    # Button Superclass: this is what specific buttons should inherit from
    button_group = pygame.sprite.Group()

    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        Button.button_group.add(self)

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
        # if clicked this button
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self):
            if self.color == (255, 255, 255):
                self.color = (255, 0, 0)
            else:
                self.color = (255, 255, 255)
            self.image.fill(self.color)


class CardButton(Button):
    # CardButton should be attribute of Card?
    card_group = pygame.sprite.Group()

    def __init__(self, pos_x, pos_y, letter):
        super().__init__(50, 70, pos_x, pos_y)
        CardButton.card_group.add(self)

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

    # on click
    def update(self):
        # if clicked this button
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self):
            if self.is_selected:
                self.deselect()
            else:
                for card in CardButton.card_group:
                    card.deselect()
                self.select()


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
