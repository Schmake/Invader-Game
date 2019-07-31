import pygame
import random
import math
from pygame.sprite import Sprite

class AmmoCrate(Sprite):

    def __init__(self, invasion_settings, screen, game_stats):
        super().__init__()

        self.invasion_settings = invasion_settings
        self.screen = screen
        self.game_stats = game_stats

        self.image = pygame.image.load('Images/ammo_crate.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(50, 1100)
        self.rect.y = random.randrange(200, 750)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):

        self.screen.blit(self.image, self.rect)



