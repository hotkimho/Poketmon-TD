import pygame
import enemy as enemy_unit
import image_init as image

import time
import math
from pygame.transform import scale
from pygame.locals import *
width = 1024
height = 910
white = (1, 100, 255)
space_x = 70
space_y = 70
global gamepad
enemy_move = [
    (0, 5),
    (11, 0),
    (0, -4),
    (-4, 0),
    (0, 11),
    (4, 0),
    (0, -4),
    (-11, 0),
    (0, 4),
    (4, 0),
    (0, -12)]


def draw_object(obj,x,y):
    gamepad.blit(obj,(x,y))


def run_game():
    global enemy_print
    enemy_x = 10
    enemy_y = 10
    move_count = 0
    x = 0
    y = 0
    enemy_print = enemy_unit.class_enemy(image.enemy1)

    crashed = False
    game_map = make_map()
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        #맵 이미지 셋팅
        for i in range(13):
            for j in range(12):
                if game_map[i][j] == 1:
                    draw_object(image.enemy_tile1, j * space_x, i * space_y)
                else:
                    draw_object(image.tile1, j * space_x, i * space_y)

        '''
        if enemy_move[move_count][0] == 0:
            if enemy_move[move_count][1] == y:
                move_count += 1
            else:
                y += 1
                for i in range(space_y):
                    enemy_y += 1
                    draw_object(image.enemy1, enemy_x, enemy_y)
                    pygame.display.update()
                    '''
       # enemy_print.enemy_move(space_x,space_y)

        pygame.display.update()
        if crashed:
            pygame.quit()


def init_game():
    #게임 판
    global gamepad


    pygame.init()
    gamepad = pygame.display.set_mode((width, height))
    pygame.display.set_caption("포켓몬 랜덤 디펜스")
    #clock = pygame.time.Clock()



def make_map():
    game_map = [
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    ]
    return game_map


if __name__ == "__main__":
    init_game()
    run_game()


