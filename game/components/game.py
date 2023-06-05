import pygame.mixer
import pygame
from game.utils.constants import BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS,MUSIC_1
from game.components.spaceship import Spaceship
from game.components.enemis.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.counter import Counter
from game.components.power_upds.power_up_manager import PowerUpManager
from game.components.configurations.volumen import Volumen

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(MUSIC_1)
        pygame.mixer.music.set_volume(0.0)
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.menu = Menu(self.screen)
        self.death_count = Counter()
        self.score = Counter()
        self.highest_score = Counter()
        self.lives = Counter()
        self.power_up_manager = PowerUpManager()
        self.livess = 2
        self.volume = Volumen()
        self.coins = Counter()
        self.coins_game= 0


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                if self.livess > 0:  
                    pygame.mixer.music.play(-1)
                    self.run()
                    
                else:
                    self.show_menu()

                    

        pygame.display.quit()
        pygame.quit()        

    def run(self):
        # Game loop: events - update - draw
        self.reset()
        pygame.mixer.music.play(-1)
        self.playing = True
        while self.playing:
            self.volume.Volumen_controls(self.screen) 
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input  = pygame.key.get_pressed()
        self.player.update(user_input,self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        self.power_up_manager.update_coins(self)



    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.lives.draw_lives(self.screen, self.player.lives,self.livess)
        self.coins.draw_coins(self.screen , self.coins_game)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.volume.Volumen_controls(self.screen)
        pygame.display.update()
        pygame.display.flip()



    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        half_screen_width = SCREEN_WIDTH // 2
        half_screen_height = SCREEN_HEIGHT // 2
        self.menu.reset_screen_color(self.screen)
    
        if self.livess <= 0:
            self.update_highest_score()
            self.menu.draw(self.screen,'Game Over. Press any key to restart')
            self.menu.draw(self.screen,f"Your score: {self.score.count}",half_screen_width, 450,)
            self.menu.draw(self.screen,f"Highest score: {self.highest_score.count}",half_screen_width, 500,)
            self.menu.draw(self.screen,f"Total deaths: {self.death_count.count}",half_screen_width, 550,)

        if self.livess == 2:
            self.menu.draw(self.screen,'Press any key to Start')

        icon = pygame.transform.scale(ICON,(80,120))
        self.screen.blit(icon,(half_screen_width -50 , half_screen_height -150))
        self.menu.update(self)
    

    
    def update_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)
    
    def reset(self):
        self.enemy_manager.reset()
        self.bullet_manager.reset()
        self.score.reset()
        self.player.reset()
        self.lives.reset()
        self.power_up_manager.reset()
        self.coins_game == 0
    


    def draw_power_up_time (self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks())/1000,2)

            if time_to_show >= 0:
                self.menu.draw(self.screen, f"{self.player.power_up_type.capitalize()} is enabled for {time_to_show} seconds ",550,50, (255,255,255) )
            else:
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.set_image()
    


