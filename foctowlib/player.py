# -*- coding: utf-8 -*-
"""The player Sprite. It will listen to user input.
"""

import pygame

import misc

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image('player.png')

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-2, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(2, 0)
