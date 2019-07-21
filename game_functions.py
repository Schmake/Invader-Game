import sys
import pygame
import random

from bullet import Bullet
from nosferatu import Nosferatu

def check_keydown_events(event, invasion_settings, screen, bounty_hunter):

    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        bounty_hunter.moving_right = True
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        bounty_hunter.moving_left = True
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        bounty_hunter.moving_up = True
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        bounty_hunter.moving_down = True


def check_keyup_events(event, invasion_settings, screen, bounty_hunter):

    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        bounty_hunter.moving_right = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        bounty_hunter.moving_left = False
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        bounty_hunter.moving_up = False
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        bounty_hunter.moving_down = False


def check_events(invasion_settings, screen, bounty_hunter, bullets, nosferatus):

    # Watch for keyboard and mouse events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, invasion_settings, screen, bounty_hunter)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, invasion_settings, screen, bounty_hunter)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            fire_bullet(invasion_settings, screen, bounty_hunter, bullets)


    """ Should find a more suitable home that check_events"""
    if random.randrange(0, 250) < 1:
        spawn_nosferatu(invasion_settings, screen, bounty_hunter, nosferatus)

def update_screen(invasion_settings, screen, bounty_hunter, nosferatus, bullets):

    # Redraw screen during each pass through loop. bg_color defines its colour in RGB terms.
    screen.fill(invasion_settings.bg_colour)

    # Redraw bullets behind Bounty Hunter and in front of screenfill
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make bounty hunter 2/2, after fill background so bounty hunter is on top
    bounty_hunter.blitme()

    # nosferatu.blitme()
    """for nosferatu in nosferatus.sprites():
        nosferatu.draw_nosferatu()"""
    for nosferatu in nosferatus.sprites():
        nosferatu.blitme()

    

    # Make most recently drawn screen visible
    pygame.display.flip()


def update_bullets(bullets, nosferatu):

    bullets.update()

    # Deletes bullet when it reaches the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    #collisions = pygame.sprite.groupcollide(bullets, nosferatu, True, True)


def fire_bullet(invasion_settings, screen, bounty_hunter, bullets):
    
    new_bullet = Bullet(invasion_settings, screen, bounty_hunter)
    bullets.add(new_bullet)


def spawn_nosferatu(invasion_settings, screen, bounty_hunter, nosferatus):

    #if random.randrange(1, 250) < 100:
    new_nosferatu = Nosferatu(invasion_settings, screen, bounty_hunter)
    nosferatus.add(new_nosferatu)

# def spawn_chance(invasion_settings, nosferatu):


