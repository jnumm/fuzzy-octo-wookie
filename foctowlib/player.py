# -*- coding: utf-8 -*-
"""The player Sprite. It will listen to user input.
"""

import random

import pygame

from . import const
from . import misc

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self._images = misc.load_sliced_sprites(170, 106, "player_ng.png")

        self.rect = self._images[0].get_rect()
        self.rect.centerx = const.DISPLAY_WIDTH / 2

        self.orig_image = self._images[0]

        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 60
        self._last_update = 0
        self._frame = 0
        self.frame_decrease = False
        
        self.jump = 0
        self.windspeed = 0

    def update(self):
        keys = pygame.key.get_pressed()
        
        if self.jump > 0 and self.jump < 30:
            self.rect.move_ip(0, -1)
            self.image = pygame.transform.scale(self.orig_image,
                    (self.image.get_width() + 1,
                    self.image.get_height() + 1))
            self.jump += 1
        elif self.jump >= 30 and self.jump < 60:
            self.rect.move_ip(0, 1)
            self.image = pygame.transform.scale(self.orig_image,
                    (self.image.get_width() - 1,
                    self.image.get_height() - 1))
            self.jump += 1
        elif self.jump == 60:
            self.image = self.orig_image
            self.jump = 0
        
        if keys[pygame.K_LEFT] and self.jump == 0:
            self.rect.move_ip(-2, 0)
        if keys[pygame.K_RIGHT] and self.jump == 0:
            self.rect.move_ip(2, 0)
        if keys[pygame.K_SPACE] and self.jump == 0:
            self.jump = 1

        if random.random() < 0.1:
            self.windspeed = random.randint(-3, 3)
        if self.windspeed > 0:
            self.rect.move_ip(self.windspeed, 0) 

        t = pygame.time.get_ticks()
        if not self.jump and t - self._last_update > self._delay:
            if self.frame_decrease:
                self._frame -= 1
            else:
                self._frame += 1

            if self._frame == len(self._images) - 1:
                self.frame_decrease = True
            elif self._frame == 0:
                self.frame_decrease = False

            print self._frame
            self.image = self._images[self._frame]
            
            
            self._last_update = t
