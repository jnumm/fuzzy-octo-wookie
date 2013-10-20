# -*- coding: utf-8 -*-
"""This is an own chopper.
"""

import pygame

from . import const
from . import misc

class Chopper(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image("chopper.png")
        self.rect.left = const.DISPLAY_WIDTH
        self.rect.centery = const.DISPLAY_HEIGTH / 2

    def update(self):
        self.rect.move_ip(-4, 0)
