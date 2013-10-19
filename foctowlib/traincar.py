# -*- coding: utf-8 -*-
"""A moving train car.
"""

import pygame

import const
import misc

class TrainCar(pygame.sprite.Sprite):
    def __init__(self, ypos=0):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image("player.png")
        self.rect.top = ypos

    def update(self):
        self.rect.move_ip(0, 2)
        if self.rect.top > const.DISPLAY_HEIGTH:
            self.rect.bottom = 0
