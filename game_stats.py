class GameStats():

    def __init__(self, invasion_settings):
        self.invasion_settings = invasion_settings
        self.reset_stats()
        #self.play_button = play_button

        self.game_active = False
        print(str(self.lives))

    def reset_stats(self):
        self.score = 0
        self.lives = 3
        self.game_active = False



