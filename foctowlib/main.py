# -*- coding: utf-8 -*-
"""This module contains the main game function.
"""

import pygame

import back
import const
from player import *
import traincar

def main():
    """This is the main game function. It will initialize and run
    the game itself.
    """
    # Initializing pygame and pygame-related variables.
    pygame.init()
    display = pygame.display.set_mode(const.DISPLAY_SIZE)
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()

    bg1 = back.Back()
    bg2 = back.Back(bg1.rect.height)

    player = Player()
    player.rect.centery = const.DISPLAY_HEIGTH / 2

    car1 = traincar.TrainCar()
    car2 = traincar.TrainCar(car1.rect.height)

    allsprites = pygame.sprite.RenderPlain((bg1, bg2, player, car1, car2))

    # This is the main loop.
    while True:
        clock.tick(60)

        # Quit the program on a pygame.QUIT event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        allsprites.update()

        display.fill((0, 0, 0))
        allsprites.draw(display)
        pygame.display.flip()
