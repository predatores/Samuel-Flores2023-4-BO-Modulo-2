import random
import pygame

from game.components.power_upds.shield import Shield,Heart,Duplicate,Coin
from game.utils.constants import SPACESHIP2, SPACESHIP_SHIELD



class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_anppears = random.randint(5000,10000)
        self.duration = random.randint(3,5)
        self.power_up_hearts = []
        self.power_up_duplicates = []
        self.power_up_coins = []
        self.when_coins = random.randint(5000,10000)
        self.coins_required = 10

    def generate_power_up(self):
        power_up = Shield()
        power_up_heart = Heart()
        self.when_anppears += random.randint(5000,10000)
        self.power_ups.append(power_up)
        self.power_up_hearts.append(power_up_heart)

        power_up_duplicate = Duplicate()
        self.power_up_duplicates.append(power_up_duplicate)

    def generate_coins(self):
            power_coin = Coin()
            self.when_anppears += random.randint(1000,5000)
            self.power_up_coins.append(power_coin)

    def update_coins(self, game):
        current_time_coin = pygame.time.get_ticks()
        if (len(self.power_up_coins) == 0 and current_time_coin >= self.when_coins):
            self.generate_coins()
        for power_coin in self.power_up_coins:
            power_coin.update(game.game_speed, self.power_up_coins)
            if game.player.rect.colliderect(power_coin.rect):
                game.player.power_up_type = power_coin.type
                game.coins_game += 1
                self.power_up_coins.remove(power_coin)

        if game.coins_game >= self.coins_required:
            game.player.set_image((75, 80), SPACESHIP2) 

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if (len(self.power_ups) == 0 or len(self.power_up_hearts) == 0 or len(self.power_up_duplicates) == 0) and current_time >= self.when_anppears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration *1000)
                game.player.set_image((80,100),SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)
        
        for power_up_heart in self.power_up_hearts:
            power_up_heart.update(game.game_speed, self.power_up_hearts)
            if game.player.rect.colliderect(power_up_heart.rect):
                game.player.power_up_type = power_up_heart.type
                game.livess += 1
                self.power_up_hearts.remove(power_up_heart)
        


        for power_up_duplicate in self.power_up_duplicates:
            power_up_duplicate.update(game.game_speed, self.power_up_duplicates)
            if game.player.rect.colliderect(power_up_duplicate.rect):
                game.player.power_up_type = power_up_duplicate.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up_duplicate.start_time + (self.duration * 1000)
                game.player.set_image((65, 75), SPACESHIP2)
                game.player.enable_duplicate()
                self.power_up_duplicates.remove(power_up_duplicate)


    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

        for power_up_heart in self.power_up_hearts:
            power_up_heart.draw(screen)

        for power_up_duplicate in self.power_up_duplicates:
            power_up_duplicate.draw(screen)

        for power_coin in self.power_up_coins:
            power_coin.draw(screen)

    def reset(self):
        self.power_ups = []
        self.power_up_hearts = []
        self.power_up_duplicates = []
        self.power_up_coins = []
        now = pygame.time.get_ticks()
        self.when_anppears = random.randint(now + 5000, now + 10000)
        self.when_coins = random.randint(now + 5000, now + 10000)

