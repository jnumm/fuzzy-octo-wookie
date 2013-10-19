# -*- coding: utf-8 -*-

import pygame

import const
import misc

class Moving(pygame.sprite.Sprite):
    """A moving object, either a background image or a train car.
    """

    def __init__(self, type, ypos=0):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if self.type == const.MOVING_BG:
            self.image, self.rect = misc.load_image("bg.png")
        elif self.type == const.MOVING_TRAINCAR:
            self.image, self.rect = misc.load_image("player.png")
        self.rect.top = ypos

    def update(self):
        if self.type == const.MOVING_BG:
            self.rect.move_ip(0, 5)
        elif self.type == const.MOVING_TRAINCAR:
            self.rect.move_ip(0, 2)

        if self.rect.top > const.DISPLAY_HEIGTH:
            self.rect.bottom = 0
