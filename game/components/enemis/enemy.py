import pygame
import random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1,SCREEN_HEIGHT,SCREEN_WIDTH,ENEMY_2,ENEMY_3,ENEMY_4
from game.components.bullets.bullet import Bullet

class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    ENEMY_WIDTH2 = 60
    ENEMY_HEIGHT2 = 80
    Y_POS = 5
    X_POS_LIST = [50,100,150,200,250,300,350,400,450,500,550,1000,900,850,750]

    SPEED_Y = 50
    SPEED_X = 10

    MOV_X = {0: 'left', 1: 'right' }
    IMAGE = { 1:ENEMY_1,2:ENEMY_2,3:ENEMY_3,4:ENEMY_4 }


    

    def __init__(self, image = 1, speed_x = SPEED_X, speed_y = SPEED_Y, move_x_for = [30,100]):
        self.image = self.IMAGE[image]
        self.image = pygame.transform.scale(self.image,(self.ENEMY_WIDTH,self.ENEMY_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0,14)]
        self.rect.y = self.Y_POS
        self.speed_y = speed_y
        self.speed_x = speed_x
        self.movement_x = self.MOV_X[random.randint(0,1)]
        self.move_x_for = random.randint(move_x_for[0], move_x_for[1])
        self.index = 0
        self.type = 'enemy'
        self.shooting_time = random.randint(30,50)
        


        


    def update(self, ships, game):
        self.shoot(game.bullet_manager)

        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        

        self.change_movement_x()


        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
        

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))


    def  change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.movement_x2 = 'right'
            self.index = 0
        if (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10 ):
            self.movement_x = 'right'
            self.index = 0


    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(30,50)