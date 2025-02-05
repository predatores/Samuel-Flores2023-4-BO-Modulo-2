import pygame
from game.utils.constants import FONT_STYLE

class Counter:
    def __init__(self):
        self.count = 0
    def update(self):
        self.count += 1

    def draw(self, screen):
        font = pygame.font.SysFont(FONT_STYLE, 32)
        text = font.render(f"Score: {self.count}", True,(255,0,0))
        text_rect = text.get_rect()
        text_rect.center = (1300,50)
        screen.blit(text, text_rect)
    
    def reset(self):
        self.count = 0

    def set_count(self, value):
        self.count = value

    def draw_lives(self, screen, lives,livess):
        font = pygame.font.SysFont(FONT_STYLE, 32)
        text = font.render(f"Lives: {lives+livess}", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1300, 100)
        screen.blit(text, text_rect)
    
    def draw_coins(self, screen, coins):
        font = pygame.font.SysFont(FONT_STYLE, 32)
        text = font.render(f"Coins: {coins}", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1300, 150)
        screen.blit(text, text_rect)
