import abc
import pygame

pygame.init()


class Cursor(pygame.sprite.Sprite):
    cursor_group = pygame.sprite.GroupSingle()

    def __init__(self):
        super().__init__()
        Cursor.cursor_group.add(self)

        # cursor hitbox
        self.rect = pygame.Rect(0, 0, 1, 1)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Button(pygame.sprite.Sprite, abc.ABC):
    # abstract button superclass
    button_group = pygame.sprite.Group()

    def __init__(self, width, height, pos_x, pos_y):
        super().__init__()
        Button.button_group.add(self)

        # button states
        self.is_selected = False
        self.is_confirmed = False
        self.is_pressed = False
        self.is_active = True

        # common scaled font for all buttons
        self.font = pygame.font.SysFont(None, int(height / 2))

        # image
        self.image = pygame.Surface((width, height))
        self.color = (255, 255, 255)
        self.image.fill(self.color)

        # rect
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    # on click
    @abc.abstractmethod
    def update(self):
        pass


class CardButton(Button):
    card_group = pygame.sprite.Group()

    def __init__(self, pos_x, pos_y, card):
        super().__init__(50, 70, pos_x, pos_y)
        CardButton.card_group.add(self)

        self.card = card

        # letter
        self.text = self.font.render(card.LETTER.upper(), False, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.image.blit(
            self.text, (25 - self.text_w / 2, 35 - self.text_h / 2))

    # on click
    def update(self):
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            if self.is_selected:
                self.is_confirmed = True
            else:
                # deselect all other cards
                for card in CardButton.card_group:
                    card.redraw(self.color)
                    card.is_selected = False
                # select current card
                self.redraw((0, 255, 0))
                self.is_selected = True

    def redraw(self, color):
        self.image.fill(color)
        self.image.blit(
            self.text, (25 - self.text_w / 2, 35 - self.text_h / 2))


class ActionButton(Button):
    def __init__(self, pos_x, pos_y, word):
        super().__init__(100, 50, pos_x, pos_y)

        self.word = word

        # word
        self.text = self.font.render(word, False, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.image.blit(
            self.text, (50 - self.text_w / 2, 25 - self.text_h / 2))

    # on click
    def update(self):
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            self.is_pressed = True
