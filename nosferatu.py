import pygame
from pygame.sprite import Sprite
import random

class Nosferatu(Sprite):

    def __init__(self, invasion_settings, screen, bounty_hunter):
        super().__init__()

        self.screen = screen
        self.invasion_settings = invasion_settings
        self.bounty_hunter = bounty_hunter


        self.image = pygame.image.load('Images/Nosferatu2.bmp')
        self.rect = self.image.get_rect()

        # Starting each enemy near top left of screen
        self.rect.x = random.randrange(-50, 1490)
        self.rect.y = -250

        # Store exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):

        self.screen.blit(self.image, self.rect)

    def update(self):
        
        self.nosferatu_displacement_x = float(self.bounty_hunter.x - self.x)
        self.nosferatu_displacement_y = float(self.bounty_hunter.y - self.y)

        nos_x = float(self.nosferatu_displacement_x)
        nos_y = float(self.nosferatu_displacement_y)
        nos_sfactor = self.invasion_settings.nosferatu_speedfactor

        if nos_x <= nos_y:

            if self.nosferatu_displacement_x <= 0:
                self.x -= float((abs(nos_x / nos_y)) * nos_sfactor)
                self.rect.x = self.x
            elif nos_x > 0:
                self.x += float((abs(nos_x / nos_y)) * nos_sfactor)
                self.rect.x = self.x

            if nos_y <= 0:
                self.y -= float((1 - (abs(nos_x / nos_y))) * nos_sfactor)
                self.rect.y = self.y
            elif nos_y > 0:
                self.y += float((1 - (abs(nos_x / nos_y))) * nos_sfactor)
                self.rect.y = self.y

        elif nos_x > nos_y:

            if nos_y <= 0:
                self.y -= float(abs((nos_y / nos_x)) * nos_sfactor)
                self.rect.y = self.y
            elif nos_y > 0:
                self.y += float(abs((nos_y / nos_x)) * nos_sfactor)
                self.rect.y = self.y

            if nos_x <= 0:
                self.x -= float((1 - abs((nos_y / nos_x))) * nos_sfactor)
                self.rect.x = self.x
            elif nos_x > 0:
                self.x += float((1 - abs((nos_y / nos_x))) * nos_sfactor)
                self.rect.x = self.x

        """elif nos_x == nos_y:
            if nos_x == 0 and nos_y == 0:
                self.rect.x = self.bounty_hunter.x
                self.rect.y = self.bounty_hunter.y
            else:
                if y >= 0:
                    self.y += (0.5 * self.invasion_settings.nosferatu_speedfactor)
                    self.rect.y = self.y
                if x >= 0:
                    self.x += (0.5 * self.invasion_settings.nosferatu_speedfactor)
                    self.rect.x = self.x"""

