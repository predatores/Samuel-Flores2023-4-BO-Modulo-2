from game.components.enemis.enemy import Enemy
import random

class EnemyManager:
    def __init__(self) :
        self.enemies = []

    def update(self, game):
        self.add_enemy()

        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            #if enemy.rect.colliderect(game.player.rect):
                #game.running = False
                #break


    def draw(self,screen):
        for enemy in self.enemies :
            enemy.draw(screen)

    def add_enemy(self):
        enemy_type = random.randint(1,4)
        if enemy_type ==1:
            enemy = Enemy()
        else:
            x_speed = 5
            y_speed = 3
            move_x_for = [50,120]
            enemy = Enemy(enemy_type, x_speed, y_speed, move_x_for)
        if len(self.enemies)  < 1:
            self.enemies.append(enemy)

    def reset(self):
        self.enemies = []

