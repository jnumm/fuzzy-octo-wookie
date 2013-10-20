# -*- coding: utf-8 -*-
"""This module contains the main game function.
"""

import pygame

from . import const
from . import moving
from .player import *

def main():
    """This is the main game function. It will initialize and run
    the game itself.
    """
    # Initializing pygame and pygame-related variables.
    pygame.init()
    display = pygame.display.set_mode(const.DISPLAY_SIZE)
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()

    bg1 = moving.Moving(const.MOVING_BG)
    bg2 = moving.Moving(const.MOVING_BG, bg1.rect.height)
    bg_sprites = pygame.sprite.RenderPlain((bg1, bg2))

    car1 = moving.Moving(const.MOVING_TRAINCAR)
    car2 = moving.Moving(const.MOVING_TRAINCAR, car1.rect.height)
    train_sprites = pygame.sprite.RenderPlain((car1, car2))

    player = Player()
    player.rect.centery = const.DISPLAY_HEIGTH / 2
    character_sprites = pygame.sprite.RenderPlain((player))

    # This is the main loop.
    while True:
        clock.tick(60)

        # Quit the program on a pygame.QUIT event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        bg_sprites.update()
        train_sprites.update()
        character_sprites.update()

        display.fill((0, 0, 0))
        bg_sprites.draw(display)
        train_sprites.draw(display)
        character_sprites.draw(display)
        pygame.display.flip()
