import random
import pygame
from game.components.power_upds.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_anppears = random.randint(5000,10000)
        self.duration = random.randint(3,5)

    def generate_power_up(self):
        power_up = Shield()
        self.when_anppears += random.randint(5000,10000)
        self.power_ups.append(power_up)

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time>= self.when_anppears:
            self.generate_power_up()


        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up.rect):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration *1000)
                game.player.set_image((65,75),SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)



    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_anppears = random.randint(now + 5000, now + 10000)
