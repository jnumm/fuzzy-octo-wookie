# -*- coding: utf-8 -*-
"""Some utility functions for the game.
"""

import os

import pygame

def load_image(name):
    """Loads an image file.
    Returns: a tuple of Image and the corresponding Rect.
    """
    fullname = os.path.join("assets", "img", name)
    image = pygame.image.load(fullname)
    #image = image.convert()
    return image, image.get_rect()
