import pygame
import random

from pygame.sprite import Sprite
from game.components.bullets import bullet_manager
from game.utils.constants import ENEMY_1,SCREEN_HEIGHT,SCREEN_WIDTH,ENEMY_2,ENEMY_3,ENEMY_4
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    ENEMY_WIDTH2 = 60
    ENEMY_HEIGHT2 = 80
    ENEMY_WIDTH3 = 80
    ENEMY_HEIGHT3 = 100
    ENEMY_WIDTH4 = 160
    ENEMY_HEIGHT4 = 180

    Y_POS = 5
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550]
    X_POS_LIST2 = [25,75,125,175,225,275,325,375,425,475,524] 
    X_POS_LIST3 = [654,750,499,800,999,1000,850,600,440,475,524] 
    X_POS_LIST4 = [1000,900,850,750] 

    SPEED_Y = 2
    SPEED_X = 30

    SPEED_Y2 = 2
    SPEED_X2 = 5

    SPEED_Y3 = 3
    SPEED_X3 = 2

    SPEED_Y4 = 9
    SPEED_X4 = 3
    MOV_X = {0: 'left', 1: 'right' }
    MOV_X4 = {0: 'right', 1: 'left' }
    IMAGE = { 1:ENEMY_1,2:ENEMY_2,3:ENEMY_3,4:ENEMY_4 }


    

    def __init__(self, image = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = [30,100]):
        self.image = self.IMAGE[image]
        self.image = pygame.transform.scale(self.image,(self.ENEMY_WIDTH,self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0,10)]
        self.rect.y = self.Y_POS
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30,50)
        
        self.image2 = ENEMY_2
        self.image2 = pygame.transform.scale(self.image2,(self.ENEMY_WIDTH2,self.ENEMY_HEIGHT2))
        self.rect2 = self.image2.get_rect()
        self.rect2.x = self.X_POS_LIST2[random.randint(0,10)]
        self.rect2.y = self.Y_POS
        self.speed_y2 = self.SPEED_Y2
        self.speed_x2 = self.SPEED_X2
        self.move_x_for_2 = random.randint(10,50)
        self.count = 0

        self.image3 = ENEMY_3
        self.image3 = pygame.transform.scale(self.image3, (self.ENEMY_WIDTH3, self.ENEMY_HEIGHT3))
        self.rect3 = self.image3.get_rect()
        self.rect3.x = self.X_POS_LIST3[random.randint(0, 10)]
        self.rect3.y = self.Y_POS
        self.speed_y3 = self.SPEED_Y3
        self.speed_x3 = self.SPEED_X3

        self.image4 = ENEMY_4
        self.image4 = pygame.transform.scale(self.image4, (self.ENEMY_WIDTH4, self.ENEMY_HEIGHT4))
        self.rect4 = self.image4.get_rect()
        self.rect4.x = self.X_POS_LIST4[random.randint(0, 3)]
        self.rect4.y = self.Y_POS
        self.speed_y4 = self.SPEED_Y4
        self.speed_x4 = self.SPEED_X4
        self.movement_x_4 = self.MOV_X4[random.randint(0,1)]
        self.move_x_for_4 = random.randint(50,200)
        self.aux = 0    


        


    def update(self, ships, game):
        self.shoot(game.bullet_manager)







        self.rect.y += self.speed_y
        self.rect2.y += self.speed_y2
        self.rect3.y += self.speed_y3
        self.rect4.y += self.speed_y4

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.rect2.y -= self.speed_y2
        else:
            self.rect.x += self.speed_x
            self.rect2.y += self.speed_y2 
        
        if self.movement_x_4 == 'left':
            self.rect4.x -= self.speed_x4
        else:
            self.rect4.x += self.speed_x4

        self.change_movement_x()
        self.change_movement_x2()
        self.change_movement_x4()

        if self.rect.y >= SCREEN_HEIGHT and self.rect2.y >= SCREEN_HEIGHT and self.rect3.y >= SCREEN_HEIGHT and self.rect4.y >= SCREEN_HEIGHT:
            ships.remove(self)
        

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.image2, (self.rect2.x, self.rect2.y))
        screen.blit(self.image3, (self.rect3.x, self.rect3.y))
        screen.blit(self.image4, (self.rect4.x, self.rect4.y))

    def  change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.movement_x2 = 'right'
            self.index = 0
        if (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10 ):
            self.movement_x = 'right'
            self.index = 0

    def  change_movement_x2(self):
        self.count +=1
        if (self.count > self.move_x_for_2 and self.rect.x <= 10):
            self.count = 0

    def  change_movement_x4(self):
        self.aux += 1
        if (self.aux >= self.move_x_for_4 and self.movement_x_4 == 'right') or (self.rect4.x >= SCREEN_WIDTH - self.ENEMY_WIDTH4):
            self.movement_x4 = 'left'
            self.aux = 0


    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30,50)