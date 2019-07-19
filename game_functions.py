import sys
import pygame

from bullet import Bullet

def check_keydown_events(event, invasion_settings, screen, bounty_hunter, bullets):

    if event.key == pygame.K_RIGHT:
        bounty_hunter.moving_right = True
    elif event.key == pygame.K_LEFT:
        bounty_hunter.moving_left = True
    elif event.key == pygame.K_UP:
        bounty_hunter.moving_up = True
    elif event.key == pygame.K_DOWN:
        bounty_hunter.moving_down = True

    if event.mouse == pygame.MOUSEBUTTONDOWN:
        new_bullet = Bullet(invasion_settings, screen, bounty_hunter)
        bullets.add(new_bullet)
        
        """fire_gun = True
        while fire_gun:
            new_bullet = Bullet(invasion_settings, screen, bounty_hunter)
            bullets.add(new_bullet)
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                fire_gun = False"""


def check_keyup_events(event, invasion_settings, screen, bounty_hunter, bullets):

    if event.key == pygame.K_RIGHT:
        bounty_hunter.moving_right = False
    elif event.key == pygame.K_LEFT:
        bounty_hunter.moving_left = False
    elif event.key == pygame.K_UP:
        bounty_hunter.moving_up = False
    elif event.key == pygame.K_DOWN:
        bounty_hunter.moving_down = False


def check_events(invasion_settings, screen, bounty_hunter, bullets):

    # Watch for keyboard and mouse events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, invasion_settings, screen, bounty_hunter, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, invasion_settings, screen, bounty_hunter, bullets)


def update_screen(invasion_settings, screen, bounty_hunter, bullets):

    # Redraw screen during each pass through loop. bg_color defines its colour in RGB terms.
    screen.fill(invasion_settings.bg_colour)

    # Redraw bullets behind Bounty Hunter and in front of screenfill
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make bounty hunter 2/2, after fill background so bounty hunter is on top
    bounty_hunter.blitme()

    # Make most recently drawn screen visible
    pygame.display.flip()


