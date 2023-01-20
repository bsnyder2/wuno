import abc
import pygame

pygame.init()


class Cursor(pygame.sprite.Sprite):
    # invisible mouse sprite class: there is only one of these objects for the whole game --> functions as our "clicker"
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

    def __init__(self, gui, width, height, pos_x, pos_y):
        super().__init__()
        Button.button_group.add(self)

        self.gui = gui

        # common scaled font for all buttons
        self.font = pygame.font.SysFont(None, int(height / 2))

        # image
        self.image = pygame.Surface((width, height))
        self.color = (255, 255, 255)
        self.image.fill(self.color)

        # rect
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

        self.is_active = True

    # on click
    @abc.abstractmethod
    def update(self):
        pass


class CardButton(Button):
    # CardButton should be attribute of Card?
    card_group = pygame.sprite.Group()

    def __init__(self, gui, pos_x, pos_y, card):
        super().__init__(gui, 50, 70, pos_x, pos_y)
        CardButton.card_group.add(self)

        self.card = card
        self.is_selected = False
        self.is_confirmed = False

        # letter
        self.text = self.font.render(card.LETTER.upper(), False, (0, 0, 0))
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
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            if self.is_selected:
                print("here")
                self.is_confirmed = True
            else:
                print(self.card)
                print("SELECT")
                for card in CardButton.card_group:
                    card.deselect()
                self.select()


class CompleteButton(Button):
    complete_group = pygame.sprite.Group()

    def __init__(self, gui, pos_x, pos_y):
        super().__init__(gui, 100, 50, pos_x, pos_y)
        CompleteButton.complete_group.add(self)

        # letter
        self.text = self.font.render("Complete", False, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.image.blit(
            self.text, (50 - self.text_w / 2, 25 - self.text_h / 2))

    # on click
    def update(self):
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            self.gui.game.run_complete()


class ChallengeButton(Button):
    challenge_group = pygame.sprite.Group()

    def __init__(self, gui, pos_x, pos_y):
        super().__init__(gui, 100, 50, pos_x, pos_y)
        CompleteButton.complete_group.add(self)
    
        # letter
        self.text = self.font.render("Challenge", False, (0, 0, 0))
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.image.blit(
            self.text, (50 - self.text_w / 2, 25 - self.text_h / 2))

    # on click
    def update(self):
        if pygame.sprite.collide_rect(Cursor.cursor_group.sprite, self) and self.is_active:
            self.gui.game.run_complete()

