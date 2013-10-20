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
        self.landing = 0
        self.orig_image = self.image

        self.chopper_snd = misc.load_sound("chopper.ogg")

    def update(self):
        self.chopper_snd.play()
        if self.landing > 0 and self.landing < 30:
            self.image = pygame.transform.scale(self.orig_image,
                    (self.image.get_width() - 1,
                    self.image.get_height() - 1))
            self.landing += 1
        elif self.landing >= 30 and self.landing < 60:
            self.image = pygame.transform.scale(self.orig_image,
                    (self.image.get_width() + 1,
                    self.image.get_height() + 1))
            self.landing += 1
        elif self.landing == 60:
            self.image = self.orig_image
            self.landing = 0
        else:
            self.rect.move_ip(-4, 0)

    def land(self):
        self.landing = 1

    def is_landing(self):
        return (self.landing > 0)

    def ready_to_pick(self):
        return (self.landing == 30)
