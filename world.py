import pygame


class Block:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 200
        self.height = 50

    def render(self, window):
        pygame.draw.rect(window, (150, 60, 60), (self.x, self.y, self.width, self.height))
