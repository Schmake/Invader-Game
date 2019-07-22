import sys
import pygame
import random
from time import sleep
# sleep(0.5)

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
    if random.randrange(0, 1000) < invasion_settings.nosferatu_spawnfactor:
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


def update_bullets(bullets, nosferatus):

    bullets.update()

    # Deletes bullet when it reaches the top of the screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    

def fire_bullet(invasion_settings, screen, bounty_hunter, bullets):
    
    new_bullet = Bullet(invasion_settings, screen, bounty_hunter)
    bullets.add(new_bullet)


def spawn_nosferatu(invasion_settings, screen, bounty_hunter, nosferatus):

    #if random.randrange(1, 250) < 100:
    new_nosferatu = Nosferatu(invasion_settings, screen, bounty_hunter)
    nosferatus.add(new_nosferatu)


def detect_collisions(invasion_settings, game_stats, screen, bullets, nosferatus, bounty_hunter):

    if pygame.sprite.spritecollideany(bounty_hunter, nosferatus):
        
        #pygame.sprite.groupcollide(bounty_hunter, nosferatus, False, True)

        bounty_hunter_hit(invasion_settings, game_stats, screen, bounty_hunter, nosferatus, bullets)
    
    # Detect collisions between bullets and enemies. 
    # Delete both if collision detected, and add 1 to player's score
    collisions = pygame.sprite.groupcollide(bullets, nosferatus, True, True)

    if collisions:
        game_stats.score += 1

def bounty_hunter_hit(invasion_settings, game_stats, screen, bounty_hunter, nosferatus, bullets):

    game_stats.lives -= 1
    nosferatus.empty()
    bullets.empty()
    print(str(game_stats.lives))

    if game_stats.lives == 0:
        nosferatus.empty()
        bullets.empty()
        sleep(1.5)
        game_stats.reset_stats()


#def enemy_killed():
