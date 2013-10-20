# -*- coding: utf-8 -*-
"""This box contains the evidence. reaching it will cause
the player to win this game.
"""

import pygame

from . import const
from . import misc

class Box(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image("box.png")
        self.rect.bottom = 0
        self.rect.centerx = const.DISPLAY_WIDTH / 2

    def update(self):
        self.rect.move_ip(0, 4)
