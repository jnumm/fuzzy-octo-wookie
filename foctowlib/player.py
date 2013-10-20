# -*- coding: utf-8 -*-
"""The player Sprite. It will listen to user input.
"""

import pygame

from . import misc

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image('player.png')
        self.jump = 0

    def update(self):
        keys = pygame.key.get_pressed()
        
        if self.jump > 0 and self.jump < 15:
            self.rect.move_ip(0, -1)
            self.jump += 1
        elif self.jump >= 15 and self.jump < 30:
            self.rect.move_ip(0, 1)
            self.jump += 1
        elif self.jump == 30:
            self.jump = 0
        
        if keys[pygame.K_LEFT]:
            self.rect.move_ip(-2, 0)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(2, 0)
        if keys[pygame.K_SPACE] and self.jump == 0:
            self.jump = 1
