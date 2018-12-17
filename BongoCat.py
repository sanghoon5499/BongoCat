import math
import pygame, sys, time
from time import *
from pygame.locals import *

pygame.init()

FPS=60
fpsClock=pygame.time.Clock()


width=500
height=400
DISPLAYSURF=pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Bongo Cat is love OwO')
background=pygame.image.load('white.jpg')

UP='up'
DOWN='down'

sprite=pygame.image.load('ah.png')
spritex=0
spritey=-150
direction=DOWN

def move(direction, sprite, spritex, spritey):
    if direction:
        if direction == K_UP:
            sprite=pygame.image.load('ah.png')
            pygame.mixer.music.stop()
        elif direction == K_DOWN:
            sprite=pygame.image.load('ah2.png')
            pygame.mixer.music.load('fook.mp3')
            pygame.mixer.music.play(1)
            

    return sprite, spritex, spritey


while True:
    DISPLAYSURF.blit(background,(0,0))

    DISPLAYSURF.blit(sprite,(spritex,spritey))

    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit() 

        if event.type == KEYDOWN:
            direction = event.key
        if event.type == KEYUP:
            if (event.key == direction):
                direction = None

    sprite, spritex, spritey = move(direction, sprite, spritex, spritey)

    pygame.display.update()
    fpsClock.tick(FPS)


    








