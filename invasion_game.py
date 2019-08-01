import pygame
from nosferatu import Nosferatu
from pygame.sprite import Group

from settings import Settings
from bounty_hunter import BountyHunter
import game_functions as gf
from game_stats import GameStats
from play_button import PlayButton
from ammo_crate import AmmoCrate

def run_game():

    pygame.init()
    invasion_settings = Settings()
    screen = pygame.display.set_mode(
        (invasion_settings.screen_width, invasion_settings.screen_height))
    pygame.display.set_caption = ("Invasion!")

    # Create the play button
    play_button = PlayButton(invasion_settings, screen, "Play")

    # Initialize game stats
    game_stats = GameStats(invasion_settings, screen)

    # Make Bounty Hunter
    bounty_hunter = BountyHunter(invasion_settings, screen)

    # Bullets group
    bullets = Group()

    # Make enemy(Nosferatu)
    nosferatus = Group()
    nosferatu = Nosferatu(invasion_settings, screen, bounty_hunter)

    # Ammo group
    ammo_crates = Group()
    ammo_crate = AmmoCrate(invasion_settings, screen, game_stats)

    while True:

        gf.check_events(invasion_settings, screen, game_stats, play_button, bounty_hunter, 
            bullets, nosferatus, ammo_crates)

        bounty_hunter.update()

        # gf.create_nosferatu(invasion_settings, screen,bounty_hunter, nosferatu) SHOULD HAVE READ THE ENTIRE TRACEBACK DUMBASS
        for nosferatu in nosferatus:
            nosferatu.update()
        
        gf.update_bullets(screen, bullets, nosferatus)

        gf.detect_collisions(invasion_settings,game_stats, screen, bullets, nosferatus, 
            bounty_hunter, ammo_crates)

        gf.update_screen(invasion_settings, screen, game_stats, bounty_hunter, nosferatus, 
            bullets, ammo_crates, play_button)

run_game()

