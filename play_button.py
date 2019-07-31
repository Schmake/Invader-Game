import pygame.font

class PlayButton():

    def __init__(self, invasion_settings, screen, message):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Properties of play button
        self.width, self.height = 200, 120
        self.button_colour = 155, 210, 180
        self.text_colour = 235, 245, 255
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Initialized button message
        self.prep_message(message)

    def prep_message(self, message):
        # Render image from message and center it on the button
        self.message_image = self.font.render(message, True, self.text_colour, self.button_colour)
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_colour, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)

