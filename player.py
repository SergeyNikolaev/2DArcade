import pygame


class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 32
        self.height = 32
        self.velocity = 0

    def jump(self, gravity, ground):
        self.velocity += gravity
        self.y -= self.velocity
        if (self.y + self.height) > ground:
            self.y = ground - self.height

    def move_left(self, speed, groundx):
        self.x -= speed
        if self.x < groundx:
            self.x = groundx

    def move_right(self, speed, groundx):
        self.x += speed
        if self.x > (groundx - self.width):
            self.x = groundx - self.width

    def update(self, gravity, groundy):
        self.velocity += gravity
        self.y -= self.velocity
        if (self.y + self.height) > groundy:
            self.velocity = 0
            self.y = groundy - self.height

    def render(self, window):
        pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.width, self.height))
