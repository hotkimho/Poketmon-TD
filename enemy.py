import image_init as image
import pygame
import math
pygame.init()
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

    def __init__(self,obj, sp,i):
        global screen
        screen = pygame.display.set_mode((1024,910), pygame.DOUBLEBUF)
        self.enemy_image = obj
        self.enemy_image = pygame.transform.scale(self.enemy_image,(50,50))
        self.x_count = 0
        self.y_count = 0
        round = 0
        self.count = 0
        self.path_count = 0
        self.x = 10
        self.y = 10 - sp
        self.limit_count = i

    def wave(self,space_x, space_y, index):
        global screen

        delta = 70 / 5
        if self.path[self.path_count][0] == 0: # Y 이동
            
            if abs(self.path[self.path_count][1]) == self.count: # 턴 이동
                self.path_count += 1
                self.count = 0
                screen.blit(self.enemy_image, (self.x, self.y))
                print(self.y,self.limit_count)
                
            elif self.path[self.path_count][1] > 0: # 아래로 이동
                self.y_count += 50
                self.y += 5
                screen.blit(self.enemy_image,(self.x,self.y))
                if self.y_count == space_y *(self.limit_count+1)  :
                    self.count += 1
                    self.y_count = 0
               
            else:   # 위로 이동
                self.y_count -= 5
                self.y -= 5
                screen.blit(self.enemy_image, (self.x, self.y))
                if self.y_count == -space_y+ self.limit_count :
                    self.count += 1
                    self.y_count = 0

        else:  # X 이동

            if abs(self.path[self.path_count][0]) == self.count: #턴 이동
                self.path_count += 1
                self.count = 0
                screen.blit(self.enemy_image, (self.x, self.y))
                pygame.display.update()
                print("X 이동")

            elif self.path[self.path_count][0] > 0: # 우측 이동
                self.x_count += 5
                self.x += 5
                screen.blit(self.enemy_image,(self.x,self.y))
                if self.x_count == + self.limit_count :
                    self.count += 1
                    self.x_count = 0

            else:   # 좌측 이동
                self.x_count -= 5
                self.x -= 5
                screen.blit(self.enemy_image, (self.x, self.y))
                if self.x_count == -space_x + self.limit_count:
                    self.count += 1
                    self.x_count = 0