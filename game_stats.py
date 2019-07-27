import pygame.font

class GameStats():

    def __init__(self, invasion_settings, screen):
        self.invasion_settings = invasion_settings
        self.screen = screen

        self.lives_colour = 150, 145, 155
        self.score_colour = 150, 145, 155
        self.font = pygame.font.SysFont(None, 42)



        self.reset_stats()

        self.game_active = False

        print(str(self.lives))
        self.score = 0
        self.lives = 3


        self.create_scoreboard

    def reset_stats(self):
        self.score = 0
        self.lives = 3
        self.game_active = False

    def create_update_scoreboard(self):
        
        self.lives_message_image = self.font.render("Lives: " + str(self.lives), False, self.lives_colour)
        self.lives_message_rect = self.lives_message_image.get_rect()
        self.lives_message_rect.x = float(45)
        self.lives_message_rect.y = float(735)

        self.screen.blit(self.lives_message_image, (self.lives_message_rect.x,self.lives_message_rect.y))

        self.score_message_image = self.font.render("Score: " + str(self.score), False, self.score_colour)
        self.score_message_rect = self.score_message_image.get_rect()
        self.score_message_rect.x = float(45)
        self.score_message_rect.y = float(685)

        self.screen.blit(self.score_message_image, (self.score_message_rect.x,self.score_message_rect.y))