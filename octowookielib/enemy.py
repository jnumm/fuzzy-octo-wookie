# -*- coding: utf-8 -*-
"""The enemy Sprite. With shooting capability.
"""

import random

import pygame

from . import bullet
from . import const
from . import misc

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._images = misc.load_sliced_sprites(100, 70, "enemy_ng.png")
        self.rect = self._images[0].get_rect()
        self.rect.centerx = const.DISPLAY_WIDTH / 2
        self.orig_image = self._images[0]
        self._frame = 0
        self.image = self._images[self._frame]

        self.shooting = False
        self.bullet = bullet.Bullet(self.rect.center, const.BULLET_DIR_DOWN)
        self.bullets = pygame.sprite.RenderPlain()

    def update(self):
        if random.random()  < 0.3:
            if random.random() < 0.5:
                self.rect.move_ip (3, 0)
            else:
                self.rect.move_ip (-3, 0)
        if random.random() > 0.1:
            self.shooting = True
            self.shoot()

        if self.shooting:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]

    def reset_bullet(self):
        self.bullet.rect.center = self.rect.center

    def shoot(self):
        if not self.bullet.alive():
            self.reset_bullet()
            self.bullets.add(self.bullet)
