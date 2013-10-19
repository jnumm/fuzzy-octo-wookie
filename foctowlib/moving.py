# -*- coding: utf-8 -*-
"""A moving backgound.
"""

import pygame

import const
import misc

class Back(pygame.sprite.Sprite):
    def __init__(self, ypos=0):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image("bg.png")
        self.rect.top = ypos
 
    def update(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > const.DISPLAY_HEIGTH:
            self.rect.bottom = 0
