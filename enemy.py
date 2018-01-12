import image_init as image
import pygame
import main
import math

class class_enemy(object):
    path = [
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


    def __init__(self, obj):
        self.enemy_image = obj
        level_count = 0
        self.count = 0
        self.path_count = 0
        move_count = 0
        self.x = 10
        self.y = 10
#        main.draw_object(self.enemy_image, 10, 10)
        print("칼르")


    def enemy_move(self,space_x, space_y):

        if self.path[self.path_count][0] == 0: # Y 이동

            if self.path[self.path_count][1] > 0: # 양수
                self.y += space_y
                main.draw_object(self.enemy_image, self.x, self.y)
            else:   #음수
                self.y -= space_y
                main.draw_object(self.enemy_image, self.x, self.y)
            self.count += 1
            pygame.display.update()
        else:  # X 이동
            if abs(self.path[self.path_count][1]) == self.count:
                self.path_count += 1
                self.count = 0

            if self.path[self.path_count][0] > 0: # 양수
                self.x += space_x
                main.draw_object(self.enemy_image, self.x, self.y)
            else:   #음수
                self.x -= space_x
                main.draw_object(self.enemy_image, self.x, self.y)

            self.count += 1
            main.draw_object(self.enemy_image,10,10)
            pygame.display.update()
