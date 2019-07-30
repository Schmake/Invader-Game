import pygame
import math
from pygame.sprite import Sprite

from bounty_hunter import BountyHunter

class Bullet(Sprite):

    def __init__(self, invasion_settings, screen, bounty_hunter):
        super().__init__()

        self.screen = screen
        self.invasion_settings = invasion_settings
        self.bounty_hunter = bounty_hunter

        # Bullet is created at (0,0) and set to correct position at Bounty Hunter
        self.rect = pygame.Rect(0,0, 
            invasion_settings.bullet_width, invasion_settings.bullet_height)
        self.rect.centerx = bounty_hunter.rect.centerx
        self.rect.centery = bounty_hunter.rect.centery

        #bullet_vector = pygame.math.Vector2(2, 3)

        # Store bullet's position as decimal

        self.x = float(self.rect[0])
        self.y = float(self.rect[1])

        self.speedfactor = invasion_settings.bullet_speedfactor
        self.colour = invasion_settings.bullet_colour

        self.first_update = True

    def update(self):
        # Update decimal position of bullet and then update then update rect position (since it can't store decimals itself)

        if self.first_update == True:
            test_vector = pygame.mouse.get_pos()
            mouse_vector = pygame.math.Vector2(float(test_vector[0]), float(test_vector[1]))
            bounty_vector = (self.bounty_hunter.x, self.bounty_hunter.y)
            bounty2_vector = pygame.math.Vector2(bounty_vector[0], bounty_vector[1])
            print(bounty2_vector)
            bullet_vector = mouse_vector - bounty2_vector
            self.normalized_vector = [(bullet_vector[0] / math.sqrt(bullet_vector[0]**2 + bullet_vector[1]**2)),
                (bullet_vector[1] / math.sqrt(bullet_vector[0]**2 + bullet_vector[1]**2))]

            self.first_update = False

        self.x += float(self.normalized_vector[0]) * self.speedfactor
        self.rect.x = self.x

        self.y += float(self.normalized_vector[1]) * self.speedfactor
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw bullet on the screen
        pygame.draw.rect(self.screen, self.colour, self.rect)

