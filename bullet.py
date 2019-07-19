import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, invasion_settings, screen, bounty_hunter):
        super().__init__()
        self.screen = screen

        # Bullet is created at (0,0) and set to correct position at Bounty Hunter
        self.rect = pygame.Rect(0,0, 
            invasion_settings.bullet_width, invasion_settings.bullet_height)
        self.rect.centerx = bounty_hunter.rect.centerx
        self.rect.top = bounty_hunter.rect.top

        # Store bullet's position as decimal
        self.y = float(self.rect.y)

        self.speedfactor = invasion_settings.bullet_speedfactor
        self.colour = invasion_settings.bullet_colour

    def update(self):
        # Update decimal position of bullet and then update then update rect position (since it can't store decimals itself)
        self.y -= self.speedfactor
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw bullet on the screen
        pygame.draw.rect(self.screen, self.colour, self.rect)

