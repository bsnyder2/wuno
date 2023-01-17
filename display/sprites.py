import pygame

pygame.init()

class Cards(pygame.sprite.Sprite):
    def __init__(self, letter = "0"):
        super().__init__()
        self.letter = letter
        self.image = pygame.Surface((125, 175), flags = pygame.SRCALPHA)
        self.rect = self.image.get_rect()

    def set_position(self, position):
        self.rect.center = position

    def set_color(self, color):
        self.image.fill(color)

    def get_letter(self):
        return self.letter

class Clicker(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.rect = self.image.get_rect()
        self.position = pygame.mouse.get_pos()
        self.click = False

    def update(self):
        self.position = pygame.mouse.get_pos()
        self.rect.update(self.position, (10, 10))
        self.click = pygame.mouse.get_pressed(num_buttons= 3)[0]
        if self.click == False:
            self.image.fill((100, 100, 100))
        if self.click == True:
            self.image.fill((255, 0, 0))
