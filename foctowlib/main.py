# -*- coding: utf-8 -*-

import pygame

import const
from player import *
import traincar

bg = pygame.image.load("assets\img\\bg.png")

def main():
    pygame.init()
    display = pygame.display.set_mode(const.DISPLAY_SIZE)

    pygame.display.set_caption("GameJam")

    player = Player()
    player.rect.centery = const.DISPLAY_HEIGTH / 2

    car1 = traincar.TrainCar()
    car2 = traincar.TrainCar(200)

    allsprites = pygame.sprite.RenderPlain((player, car1, car2))

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                return

        allsprites.update()

        display.fill((0, 0, 0))
        display.blit(bg, (0, 0))
        allsprites.draw(display)
        pygame.display.flip()
