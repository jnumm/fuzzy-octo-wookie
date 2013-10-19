# -*- coding: utf-8 -*-

import os

import pygame

def load_image(name):
    fullname = os.path.join("assets", "img", name)
    image = pygame.image.load(fullname)
    #image = image.convert()
    return image, image.get_rect()
