import pygame
from nosferatu import Nosferatu
from pygame.sprite import Group

from settings import Settings
from bounty_hunter import BountyHunter
import game_functions as gf

def run_game():

    pygame.init()
    invasion_settings = Settings()
    screen = pygame.display.set_mode(
        (invasion_settings.screen_width, invasion_settings.screen_height))
    pygame.display.set_caption = ("Invasion!")

    # Make Bounty Hunter
    bounty_hunter = BountyHunter(invasion_settings, screen)

    # Bullet group
    bullets = Group()

    # Make enemy(Nosferatu)
    nosferatu = Nosferatu(invasion_settings, screen, bounty_hunter)
    """nosferatu.x = (bounty_hunter.center - nosferatu.x)
    nosferatu.rect.x = nosferatu.x

    nosferatu.y = (bounty_hunter.bottom - nosferatu.y)
    nosferatu.rect.y = nosferatu.y"""

    while True:
        gf.check_events(invasion_settings, screen, bounty_hunter, bullets)
        bounty_hunter.update()
        gf.update_bullets(bullets, nosferatu)
        nosferatu.update()
        gf.update_screen(invasion_settings, screen, bounty_hunter, nosferatu, bullets)

run_game()

