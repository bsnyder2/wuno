import pygame
import sys

pygame.init()

Card_Imgs= {"a": pygame.image.load(sys.path[0] + "/flame pngs/A.png"),
    "b": pygame.image.load(sys.path[0] + "/flame pngs/B.png"),
    "c": pygame.image.load(sys.path[0] + "/flame pngs/C.png"),
    "d": pygame.image.load(sys.path[0] + "/flame pngs/D.png"),
    "e": pygame.image.load(sys.path[0] + "/flame pngs/E.png"),
    "f": pygame.image.load(sys.path[0] + "/flame pngs/F.png"),
    "g": pygame.image.load(sys.path[0] + "/flame pngs/G.png"),
    "h": pygame.image.load(sys.path[0] + "/flame pngs/H.png"),
    "i": pygame.image.load(sys.path[0] + "/flame pngs/I.png"),
    "j": pygame.image.load(sys.path[0] + "/flame pngs/J.png"),
    "k": pygame.image.load(sys.path[0] + "/flame pngs/K.png"),
    "l": pygame.image.load(sys.path[0] + "/flame pngs/L.png"),
    "m": pygame.image.load(sys.path[0] + "/flame pngs/M.png"),
    "n": pygame.image.load(sys.path[0] + "/flame pngs/N.png"),
    "o": pygame.image.load(sys.path[0] + "/flame pngs/O.png"),
    "p": pygame.image.load(sys.path[0] + "/flame pngs/P.png"),
    "q": pygame.image.load(sys.path[0] + "/flame pngs/Q.png"),
    "r": pygame.image.load(sys.path[0] + "/flame pngs/R.png"),
    "s": pygame.image.load(sys.path[0] + "/flame pngs/S.png"),
    "t": pygame.image.load(sys.path[0] + "/flame pngs/T.png"),
    "u": pygame.image.load(sys.path[0] + "/flame pngs/U.png"),
    "v": pygame.image.load(sys.path[0] + "/flame pngs/V.png"),
    "w": pygame.image.load(sys.path[0] + "/flame pngs/W.png"),
    "x": pygame.image.load(sys.path[0] + "/flame pngs/X.png"),
    "y": pygame.image.load(sys.path[0] + "/flame pngs/Y.png"),
    "z": pygame.image.load(sys.path[0] + "/flame pngs/Z.png")}

class Cards(pygame.sprite.Sprite):
    def __init__(self, text = "0"):
        super().__init__()
        self.text = text
        self.image = pygame.image.load(sys.path[0] + "/flame pngs/A.png")
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
