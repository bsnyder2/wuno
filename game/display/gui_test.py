import pygame


class GUI:
    def __init__(self, game):
        self.game = game

    def update_hand(self):
        for hand in self.game.hands:
            print(hand)
