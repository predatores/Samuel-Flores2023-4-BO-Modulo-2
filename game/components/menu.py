import pygame
from game.utils.constants import FONT_STYLE,SCREEN_WIDTH,SCREEN_HEIGHT

class Menu:
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    
    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.text = self.font.render(message, True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

        self.score_text = self.font.render("", True, (0, 0, 0))
        self.score_text_rect = self.score_text.get_rect()

        self.max_score_text = self.font.render("", True, (0, 0, 0))
        self.max_score_text_rect = self.max_score_text.get_rect()

        self.deaths_text = self.font.render("", True, (0, 0, 0))
        self.deaths_text_rect = self.deaths_text.get_rect()
        

    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)

    def draw(self, screen):
        screen.blit(self.text, self.text_rect)
        screen.blit(self.score_text, self.score_text_rect)
        screen.blit(self.max_score_text, self.max_score_text_rect)
        screen.blit(self.deaths_text, self.deaths_text_rect)
        
    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.playing = False
                game.running = False
            elif event.type == pygame.KEYDOWN:
                game.run()
    
    def reset_screen_color(self, screen):
        screen.fill((255, 255, 255))


    def update_message(self, message, message1, message2,message3):
        self.text = self.font.render(message,True,(0,0,0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT)

        self.score_text = self.font.render(message1, True, (0, 0, 0))
        self.score_text_rect = self.text.get_rect()
        self.score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 50)

        self.max_score_text = self.font.render(message2, True, (0, 0, 0))
        self.max_score_text_rect = self.text.get_rect()
        self.max_score_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 100)

        self.deaths_text = self.font.render(message3, True, (0, 0, 0))
        self.deaths_text_rect = self.text.get_rect()
        self.deaths_text_rect.center = (self.HALF_SCREEN_WIDTH, self.HALF_SCREEN_HEIGHT + 150)


        


       
        
        

