# -*- coding: utf-8 -*-

import pygame

import misc

class TrainCar(pygame.sprite.Sprite):
    def __init__(self, ypos, display_heigth):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = misc.load_image("player.png")
        self.rect.top = ypos
        self.display_heigth = display_heigth

    def update(self):
        self.rect.move_ip(0, 2)
        if self.rect.top > self.display_heigth:
            self.rect.bottom = 0
