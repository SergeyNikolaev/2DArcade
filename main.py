import sys
import pygame
from world import *
from player import Player
pygame.init()

SPEED = 1
GRAVITY = -0.5
BLACK = (0, 0, 0)
BLUE = (50, 60, 150)

clock = pygame.time.Clock()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption('2DArcade')

player = Player(400, 100)
block = Block(300, 500)


font = pygame.font.Font(None, 36)
text = font.render(str(player.y), 1, (10, 10, 10))

textGravPos = text.get_rect()
textGravPos.centerx = 50
textGravPos.centery = 30

textpos = text.get_rect()
textpos.centerx = 50
textpos.centery = 50

textPlayerPos = text.get_rect()
textPlayerPos.centerx = 50
textPlayerPos.centery = 70


gameLoop = True
while gameLoop:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameLoop = False

    window.fill(BLUE)
    player.update(GRAVITY, block.y)
    block.render(window)
    player.render(window)

    if pygame.key.get_focused:
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_DOWN]:
            player.update(GRAVITY, block.y)
        if pressed[pygame.K_UP]:
            player.velocity = 0
            player.jump(GRAVITY, block.width)
        if pressed[pygame.K_LEFT]:
            player.move_left(SPEED, block.x)
        if pressed[pygame.K_RIGHT]:
            player.move_right(SPEED, block.x+block.width)

    textGrav = font.render('velocity = ' + str(player.velocity), 1, (10, 10, 10))
    textblock = font.render('block = ' + str(block.y), 1, (10, 10, 10))
    textplayer = font.render('player = ' + str(player.y), 1, (10, 10, 10))

    window.blit(textGrav, textGravPos)
    window.blit(textblock, textpos)
    window.blit(textplayer, textPlayerPos)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
