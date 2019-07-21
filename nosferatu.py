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
        self.rect.x = random.randrange(0, 1200)
        self.rect.y = 0

        # Store exact position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        
        self.nosferatu_displacement_x = (self.bounty_hunter.x - self.x)
        self.nosferatu_displacement_y = (self.bounty_hunter.y - self.y)
        
        if self.nosferatu_displacement_x <= self.nosferatu_displacement_y:

            if self.nosferatu_displacement_x <= 0:
                self.x -= (abs(self.nosferatu_displacement_x / self.nosferatu_displacement_y)) * self.invasion_settings.nosferatu_speedfactor
                self.rect.x = self.x
            elif self.nosferatu_displacement_x > 0:
                self.x += (abs(self.nosferatu_displacement_x / self.nosferatu_displacement_y)) * self.invasion_settings.nosferatu_speedfactor
                self.rect.x = self.x

            if self.nosferatu_displacement_y <= 0:
                self.y -= (1 - (abs(self.nosferatu_displacement_x / self.nosferatu_displacement_y))) * self.invasion_settings.nosferatu_speedfactor
                self.rect.y = self.y
            elif self.nosferatu_displacement_y > 0:
                self.y += (1 - (abs(self.nosferatu_displacement_x / self.nosferatu_displacement_y))) * self.invasion_settings.nosferatu_speedfactor
                self.rect.y = self.y

        elif self.nosferatu_displacement_x > self.nosferatu_displacement_y:

            if self.nosferatu_displacement_y <= 0:
                self.y -= abs((self.nosferatu_displacement_y / self.nosferatu_displacement_x)) * self.invasion_settings.nosferatu_speedfactor
                self.rect.y = self.y
            elif self.nosferatu_displacement_y > 0:
                self.y += abs((self.nosferatu_displacement_y / self.nosferatu_displacement_x)) * self.invasion_settings.nosferatu_speedfactor
                self.rect.y = self.y

            if self.nosferatu_displacement_x <= 0:
                self.x -= (1 - abs((self.nosferatu_displacement_y / self.nosferatu_displacement_x))) * self.invasion_settings.nosferatu_speedfactor
                self.rect.x = self.x
            elif self.nosferatu_displacement_x > 0:
                self.x += (1 - abs((self.nosferatu_displacement_y / self.nosferatu_displacement_x))) * self.invasion_settings.nosferatu_speedfactor
                self.rect.x = self.x

        """elif self.nosferatu_displacement_x == self.nosferatu_displacement_y:
            if self.nosferatu_displacement_x == 0 and self.nosferatu_displacement_y == 0:
                self.rect.x = self.bounty_hunter.center
                self.rect.y = self.bounty_hunter.bottom
            else:
                if y
                    self.y += (0.5 * self.invasion_settings.nosferatu_speedfactor)
                    self.rect.y = self.y
                    self.x += (0.5 * self.invasion_settings.nosferatu_speedfactor)
                    self.rect.x = self.x"""

