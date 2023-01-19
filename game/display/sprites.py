import pygame
from display.buttons import CardButton

pygame.init()

class Cards():
    def __init__(self, letter = "0"):
        self.letter = letter
        self.card_button = CardButton(self.letter)
        
        self.image = pygame.Surface((125, 175), flags = pygame.SRCALPHA)
        self.size = (125, 175)
        self.rect = self.image.get_rect()

    def set_position(self, position):
        self.rect.update((position), self.size)

    def set_size(self, size):
        self.image = pygame.Surface((size[0], size[1]), flags = pygame.SRCALPHA)
        self.size = size
        self.rect = self.image.get_rect()

    def get_letter(self):
        return self.letter

class Cursor(pygame.sprite.Sprite):
    # invisible mouse sprite class: there is only one of these objects for the whole game --> functions as our "clicker"

    def __init__(self):
        super().__init__()
        # cursor hitbox
        self.rect = pygame.Rect(0, 0, 1, 1)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
