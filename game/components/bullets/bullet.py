import pygame
from pygame.sprite import  Sprite
from game.utils.constants import BULLET,BULLET_ENEMY,SCREEN_HEIGHT

class Bullet(Sprite):
    BULLET_SIZE = pygame.transform.scale(BULLET,(20,50))
    BULLET_ENEMY_SIZE = pygame.transform.scale(BULLET_ENEMY,(20,50))
    BULLETS = {'player':BULLET_SIZE, 'enemy':BULLET_ENEMY_SIZE }
    SPEED = 2

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self):
        self.rect.y += self.SPEED
        if self.rect.y >= SCREEN_HEIGHT:
            self.bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))