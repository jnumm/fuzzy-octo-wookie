# -*- coding: utf-8 -*-
"""This module contains the main game function.
"""

import os
import random

import pygame

from . import box
from . import chopper
from . import const
from . import enemy
from . import moving
from .player import *

def main():
    """This is the main game function. It will initialize and run
    the game itself.
    """
    # Initializing random.
    random.seed()
    # Initializing pygame and pygame-related variables.
    pygame.mixer.pre_init(44100, -16, 2)
    pygame.init()
    display = pygame.display.set_mode(const.DISPLAY_SIZE)
    pygame.display.set_caption("Fuzzy Octo-Wookie :: JGJ '13")
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

    enemy1 = enemy.Enemy()
    character_sprites = pygame.sprite.RenderPlain((player, enemy1))

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
        enemy1.bullets.update()
        if ((not car1.rect.contains(player.rect) and
                not car2.rect.contains(player.rect) and
                player.jump == 0) or
                (player.rect.contains(enemy1.bullet.rect) and
                player.jump == 0)):
            player.dying()
            mainloop = False
            gameoverloop = True

        if not the_box.alive() and pygame.time.get_ticks() > 90000:
            character_sprites.add(the_box)

        if the_box.alive() and the_box.rect.colliderect(player.rect):
            mainloop = False
            gamewonloop = True

        display.fill((0, 0, 0))
        bg_sprites.draw(display)
        train_sprites.draw(display)
        enemy1.bullets.draw(display)
        character_sprites.draw(display)
        pygame.display.flip()
    
    if gamewonloop:
        win_or_not = "YOU WON!"
        reason = ""
    else:
        win_or_not = "GAME OVER"
        reason = "You died."
    
    while gamewonloop:
        clock.tick(60)
        # Quit the program on a pygame.QUIT event.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if (not choppa.is_landing() and
                choppa.rect.contains(player.rect) and
                player.alive() and the_box.alive()):
            choppa.land()
        
        if (choppa.ready_to_pick() and
                player.alive() and the_box.alive()):
            player.kill()
            the_box.kill()

        if choppa.rect.right < 0:
            gamewonloop = False
            gameoverloop = True
        
        chopper_sprites.update()

        display.fill((0, 0, 0))
        bg_sprites.draw(display)
        train_sprites.draw(display)
        character_sprites.draw(display)
        chopper_sprites.draw(display)
        pygame.display.flip()

    f_large = pygame.font.Font(None, 100)
    f_small = pygame.font.Font(None, 80)
    f_extrasmall = pygame.font.Font(None, 50)
    gameovertexts = [
        [f_large.render(win_or_not, True, (255, 255, 255)), 100],
        [f_extrasmall.render(reason, True, (255, 255, 255)), 160],
        [f_extrasmall.render("Credits", True, (255, 255, 255)), 300],
        [f_small.render("Juhani . code", True, (255, 255, 255)), 350],
        [f_small.render("Tuomas . code", True, (255, 255, 255)), 410],
        [f_small.render("Petteri . gfx", True, (255, 255, 255)), 470],
        [f_extrasmall.render("Music used with permission of", True, (255, 255, 255)), 550],
        [f_small.render("Heikki Anttonen", True, (255, 255, 255)), 600],
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
