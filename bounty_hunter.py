import pygame

class BountyHunter():

    def __init__(self, invasion_settings, screen):

        self.screen = screen
        self.invasion_settings = invasion_settings

        # Load bounty hunter and get rect (rects are the rectangles that represent game elements)
        self.image = pygame.image.load('Images/BountyHunter.bmp')

        #pygame.transform.scale(self.image, (20,20))
        
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each bounty hunter at the bottom of the screen (can also use top, left, right)
        #and at the center of the screen (can also use center or centery)
        """self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom"""

        # Decimal value for bounty hunter's center
        self.x = float(400)
        print(self.x)
        self.y = float(400)
        print(self.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.invasion_settings.bounty_hunter_speedfactor
        if self.moving_left and self.rect.left > 0:
            self.x -= self.invasion_settings.bounty_hunter_speedfactor
        if self.moving_up and self.rect.top > 0:
            self.y -= self.invasion_settings.bounty_hunter_speedfactor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.invasion_settings.bounty_hunter_speedfactor

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        # Draw ship at current location
        self.screen.blit(self.image, self.rect)

