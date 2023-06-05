import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1400
FPS = 45
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
MUSIC_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "Music")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

COIN = pygame.image.load(os.path.join(IMG_DIR, 'Other/boom.png'))
DUPLICATE = pygame.image.load(os.path.join(IMG_DIR, 'Other/duplicate.png'))


DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'
DUPLICATE_TYPE = 'duplicate'
COIN_TYPE = 'coin'


SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP2 = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship2.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_SHIELD1= pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship2.png"))
BULLET_NEW = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_4.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
ENEMY_3 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png"))
ENEMY_4 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png"))


MUSIC_1 = os.path.join(MUSIC_DIR, "music1.mp3")
MUSIC_UP = pygame.image.load(os.path.join(MUSIC_DIR, "music01.png"))
MUSIC_DOWN = pygame.image.load(os.path.join(MUSIC_DIR, "music02.png"))
MUSIC_MUTE = pygame.image.load(os.path.join(MUSIC_DIR, "music03.png"))
MUSIC_MAX = pygame.image.load(os.path.join(MUSIC_DIR, "music07.png"))


FONT_STYLE = 'freesansbold.ttf'
