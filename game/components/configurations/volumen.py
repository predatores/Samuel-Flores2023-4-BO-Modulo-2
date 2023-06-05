import pygame.mixer
from game.utils.constants import MUSIC_UP, MUSIC_DOWN, MUSIC_MUTE, MUSIC_MAX

class Volumen:
    def __init__(self):
        self.set_volume(0)


    def Volumen_controls(self, screen):  
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and pygame.mixer.music.get_volume() >= 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
            screen.blit(MUSIC_DOWN, (50, 50))
        elif keys[pygame.K_1] and pygame.mixer.music.get_volume() == 0.0:
            screen.blit(MUSIC_MUTE, (50, 50))

        elif keys[pygame.K_2] and pygame.mixer.music.get_volume() >= 0.0:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.02)
            screen.blit(MUSIC_UP, (50, 50))
        elif keys[pygame.K_2] and pygame.mixer.music.get_volume() == 1.0:
            screen.blit(MUSIC_MAX, (50, 50))
        elif keys[pygame.K_3]:
            pygame.mixer.music.set_volume(0.0)
            screen.blit(MUSIC_MUTE, (50, 50))
        elif keys[pygame.K_4]:
            pygame.mixer.music.set_volume(1.0)
            screen.blit(MUSIC_MAX, (50, 50))
        elif keys[pygame.K_5]:
            pygame.mixer.music.pause()
            screen.blit(MUSIC_MAX, (50, 50))
        elif keys[pygame.K_6]:
            pygame.mixer.music.play()
            screen.blit(MUSIC_MAX, (50, 50))


    def set_volume(self, volume_level):
        pygame.mixer.music.set_volume(volume_level)