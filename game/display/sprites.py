import abc
import sys
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

        # button click sound
        self.sound = pygame.mixer.Sound(
            sys.path[0] + "/assets/sounds/button-click.wav")

        # button states
        self.is_selected = False
        self.is_confirmed = False
        self.is_pressed = False
        self.is_active = True

        # image
        self.image = pygame.Surface((width, height))

        # rect
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    # on click
    @abc.abstractmethod
    def update(self):
        pass


class CardButton(Button):
    card_group = pygame.sprite.Group()

    def __init__(self, card, is_hidden, pos_x=0, pos_y=0):
        super().__init__(50, 70, pos_x, pos_y)
        CardButton.card_group.add(self)

        self.card = card
        self.is_hidden = is_hidden

        # image
        self.image.fill((160, 200, 240))
        pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 50, 70), 2)

        font = pygame.font.Font(
            sys.path[0] + "/assets/fonts/LEMONMILK-Regular.otf", 30)
        self.text = font.render(card.LETTER.upper(), True, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        # draw text if card is not hidden
        if self.is_hidden:
            self.is_active = False
        else:
            self.image.blit(
                self.text, (25 - self.text_w / 2, 35 - self.text_h / 2))

    # on click
    def update(self):
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            self.sound.play()
            if self.is_selected:
                self.is_confirmed = True
            else:
                # deselect all other cards
                for card_button in CardButton.card_group:
                    if not card_button.is_hidden:
                        card_button.image.fill((160, 200, 240))
                        pygame.draw.rect(card_button.image, (0, 0, 0), (0, 0, 50, 70), 2)
                        card_button.image.blit(
                            card_button.text, (25 - card_button.text_w / 2, 35 - card_button.text_h / 2))
                        card_button.is_selected = False
                # select current card
                self.image.fill((110, 150, 190))
                pygame.draw.rect(self.image, (0, 0, 0), (0, 0, 50, 70), 2)
                self.image.blit(
                    self.text, (25 - self.text_w / 2, 35 - self.text_h / 2))
                self.is_selected = True


class ActionButton(Button):
    def __init__(self, word, pos_x, pos_y):
        super().__init__(100, 50, pos_x, pos_y)

        self.WORD = word

        # image
        self.image.fill((255, 255, 255))
        font = pygame.font.Font(
            sys.path[0] + "/assets/fonts/LEMONMILK-Regular.otf", 15)
        self.text = font.render(self.WORD, True, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.image.blit(
            self.text, (50 - self.text_w / 2, 25 - self.text_h / 2))

    # on click
    def update(self):
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            self.sound.play()
            self.is_pressed = True


class DeckButton(Button):
    def __init__(self, pos_x, pos_y):
        super().__init__(50, 70, pos_x, pos_y)

        # image
        self.image.fill((160, 200, 240))

    def update(self):
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            self.sound.play()
            self.is_pressed = True