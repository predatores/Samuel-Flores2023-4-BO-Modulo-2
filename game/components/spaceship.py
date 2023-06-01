import pygame
from pygame.sprite import Sprite
from game.utils.constants import SPACESHIP,SCREEN_WIDTH,SCREEN_HEIGHT


class Spaceship(Sprite):
    SHIP_WIDTH = 40
    SHIP_HEIGHT = 40
    X_POS = (SCREEN_WIDTH // 2) - SHIP_WIDTH
    Y_POS = 500
    SHIP_SPEED = 25

    def __init__(self) :
        self.image = SPACESHIP
        self.image = pygame.transform.scale(self.image,(self.SHIP_WIDTH,self.SHIP_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.type = 'player'

    def update(self, user_input):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        elif user_input[pygame.K_z]:
            pygame.display.quit()
            
    def move_left(self):
        self.rect.x -= self.SHIP_SPEED
        if self.rect.right<=self.SHIP_WIDTH:
            self.rect.x = SCREEN_WIDTH - self.SHIP_HEIGHT

    def move_right(self):
        self.rect.x += self.SHIP_SPEED  
        if self.rect.left >= SCREEN_WIDTH - self.SHIP_WIDTH :
            self.rect.x = 0     

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= self.SHIP_SPEED  
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 70:
            self.rect.y += self.SHIP_SPEED    


    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))