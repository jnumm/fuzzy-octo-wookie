# -*- coding: utf-8 -*-
"""This module contains the main game function.
"""

import os

import pygame

from . import box
from . import chopper
from . import const
from . import moving
from .player import *

def main():
    """This is the main game function. It will initialize and run
    the game itself.
    """
    # Initializing pygame and pygame-related variables.
    pygame.mixer.pre_init(44100, -16, 2)
    pygame.init()
    display = pygame.display.set_mode(const.DISPLAY_SIZE)
    pygame.display.set_caption("GameJam")
    clock = pygame.time.Clock()

    mainloop = True
    gameoverloop = False
    gamewonloop = False

    bg1 = moving.Moving(const.MOVING_BG)
    bg2 = moving.Moving(const.MOVING_BG, bg1.rect.height)
    bg_sprites = pygame.sprite.RenderPlain((bg1, bg2))

    car1 = moving.Moving(const.MOVING_TRAINCAR)
    car2 = moving.Moving(const.MOVING_TRAINCAR, car1.rect.height)
    train_sprites = pygame.sprite.RenderPlain((car1, car2))

    player = Player()
    player.rect.centery = const.DISPLAY_HEIGTH / 2
    character_sprites = pygame.sprite.RenderPlain((player))

    the_box = box.Box()

    choppa = chopper.Chopper()
    chopper_sprites =  pygame.sprite.RenderPlain((choppa))

    pygame.mixer.music.load(os.path.join("assets", "snd", "music.mp3"))
    pygame.mixer.music.play(-1)

    # This is the main loop.
    while mainloop:
        clock.tick(60)

        # Quit the program on a pygame.QUIT event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        bg_sprites.update()
        train_sprites.update()
        character_sprites.update()
        if (not car1.rect.contains(player.rect) and
                not car2.rect.contains(player.rect) and
                player.jump == 0):
            mainloop = False
            gameoverloop = True

        if not the_box.alive() and pygame.time.get_ticks() > 3000:
            character_sprites.add(the_box)

        if the_box.alive() and the_box.rect.colliderect(player.rect):
            mainloop = False
            gamewonloop = True

        display.fill((0, 0, 0))
        bg_sprites.draw(display)
        train_sprites.draw(display)
        character_sprites.draw(display)
        pygame.display.flip()

    while gamewonloop:
        clock.tick(60)
        # Quit the program on a pygame.QUIT event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if choppa.rect.contains(player.rect):
            player.kill()
            the_box.kill()
        
        chopper_sprites.update()

        display.fill((0, 0, 0))
        bg_sprites.draw(display)
        train_sprites.draw(display)
        character_sprites.draw(display)
        chopper_sprites.draw(display)
        pygame.display.flip()

    f_large = pygame.font.Font(None, 100)
    f_small = pygame.font.Font(None, 80)
    f_extrasmall = pygame.font.Font(None, 70)
    gameovertexts = [
        [f_large.render("GAME OVER", True, (255, 255, 255)), 100],
        [f_extrasmall.render("Credits", True, (255, 255, 255)), 290],
        [f_small.render("Juhani", True, (255, 255, 255)), 350],
        [f_small.render("Tuomas", True, (255, 255, 255)), 410],
        [f_small.render("Petteri", True, (255, 255, 255)), 470]
    ]

    while gameoverloop:
        clock.tick(60)
        # Quit the program on a pygame.QUIT event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        display.fill((0, 0, 0))
        bg_sprites.draw(display)
        train_sprites.draw(display)
        character_sprites.draw(display)
        for text in gameovertexts:
            display.blit(text[0],
                    ((display.get_width() - text[0].get_width()) / 2,
                    text[1]))
        pygame.display.flip()
