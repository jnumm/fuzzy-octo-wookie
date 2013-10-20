# -*- coding: utf-8 -*-
"""A god-damn bullet.
"""

import pygame

from . import const
from . import misc

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image("bullet.png")
        self.rect.center = pos
        self.dir = direction
        if self.dir == const.BULLET_DIR_DOWN:
            self.image = pygame.transform.rotate(self.image, 180)

    def update(self):
        if self.dir == const.BULLET_DIR_DOWN:
            self.rect.move_ip(0, 7)
        elif self.dir == const.BULLET_DIR_UP:
            self.rect.move_ip(0, -7)

        if self.rect.top > const.DISPLAY_WIDTH or self.rect.bottom < 0:
            self.kill()
