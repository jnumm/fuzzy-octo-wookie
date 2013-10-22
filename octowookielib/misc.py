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

def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join("assets", "snd", name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error, message:
        print "Cannot load sound: ", fullname
        raise SystemExit, message
    return sound

# From http://shinylittlething.com/2009/07/21/pygame-and-animated-sprites/
def load_sliced_sprites(w, h, filename):
    '''
    Specs :
    	Master can be any height.
    	Sprites frames width must be the same width
    	Master width must be len(frames)*frame.width
    Assuming you resources directory is named "resources"
    '''
    images = []
    master_image = pygame.image.load(os.path.join("assets", "img", filename)).convert_alpha()
    
    master_width, master_height = master_image.get_size()
    for i in xrange(int(master_width/w)):
    	images.append(master_image.subsurface((i*w,0,w,h)))
    return images
