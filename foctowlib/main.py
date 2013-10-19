# -*- coding: utf-8 -*-

import pygame

from misc import *

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGTH = 640, 800

ukko = pygame.image.load("C:\Users\Pelitalo\Documents\GameJam\\assets\img\player.png")
bg = pygame.image.load("assets\img\\bg.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('player.png')
        self.rect.centery = DISPLAY_HEIGTH / 2

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-2, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(2, 0)

def main():
    pygame.init()
    display = pygame.display.set_mode(DISPLAY_SIZE)

    pygame.display.set_caption("GameJam")
    
    sijainti = [50, 50]

    player = Player()
    allsprites = pygame.sprite.RenderPlain((player))
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                return
        
        allsprites.update()

        display.blit(bg, (0, 0))
        display.blit(ukko, sijainti)
        allsprites.draw(display)
        pygame.display.flip()
