import sys
import pygame
import random
from time import sleep

from bullet import Bullet
from nosferatu import Nosferatu
from ammo_crate import AmmoCrate

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

def check_events(invasion_settings, screen, game_stats, play_button, 
    bounty_hunter, bullets, nosferatus, ammo_crates):

    # Watch for keyboard and mouse events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, invasion_settings, screen, bounty_hunter)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, invasion_settings, screen, bounty_hunter)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            fire_bullet(invasion_settings, game_stats, screen, bounty_hunter, bullets)

        if game_stats.game_active == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(game_stats, play_button, mouse_x, mouse_y)

    """ Should find a more suitable home that check_events"""
    if random.randrange(0, 1000) < invasion_settings.nosferatu_spawnfactor:
        spawn_nosferatu(invasion_settings, screen, game_stats, bounty_hunter, nosferatus)

    if game_stats.score % 20 == 0 and len(ammo_crates) < 1 and game_stats.score != invasion_settings.ammo_count:
        spawn_ammo_crate(invasion_settings, screen, game_stats, ammo_crates)
        invasion_settings.ammo_count = game_stats.score

    if (game_stats.score - game_stats.hidden_score) % 50 == 0 and game_stats.score != game_stats.hidden_score:
        game_stats.hidden_score += 50
        invasion_settings.level += 1
        level_up(invasion_settings, screen, game_stats)
        
def check_play_button(game_stats, play_button, mouse_x, mouse_y):

    if play_button.rect.collidepoint(mouse_x, mouse_y):
        game_stats.game_active = True

def update_screen(invasion_settings, screen, game_stats, bounty_hunter, 
    nosferatus, bullets, ammo_crates, play_button):

    # Redraw screen during each pass through loop. bg_color defines its colour in RGB terms.
    screen.fill(invasion_settings.bg_colour)

    game_stats.create_update_scoreboard()

    # Redraw bullets behind Bounty Hunter and in front of screenfill
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Make bounty hunter 2/2, after fill background so bounty hunter is on top
    bounty_hunter.blitme()

    # nosferatu.blitme()
    for nosferatu in nosferatus.sprites():
        nosferatu.blitme()

    for ammo_crate in ammo_crates.sprites():
        ammo_crate.blitme()

    if not game_stats.game_active:
        play_button.draw_button()

    # Make most recently drawn screen visible
    pygame.display.flip()

def update_bullets(screen, bullets, nosferatus):

    bullets.update()
    screen_rect = screen.get_rect()

    # Deletes bullet when it reaches the top of the screen
    for bullet in bullets.copy():
        #if bullet.rect.bottom <= 0 or bullet.rect.top > 800 or bullet.rect.x <= 0 or bullet.rect.x > 1200:
        if bullet.rect.bottom <= screen_rect.top or bullet.rect.bottom > screen_rect.bottom or bullet.rect.x < screen_rect.left or bullet.rect.x > screen_rect.right:
            bullets.remove(bullet)

def fire_bullet(invasion_settings, game_stats, screen, bounty_hunter, bullets):

    if invasion_settings.ammo > 0:
        new_bullet = Bullet(invasion_settings, screen, bounty_hunter)
        bullets.add(new_bullet)
        if game_stats.game_active == True:
            invasion_settings.ammo -= 1

def spawn_nosferatu(invasion_settings, screen, game_stats, bounty_hunter, 
    nosferatus):

    #if random.randrange(1, 250) < 100:
    if game_stats.game_active == True:
        new_nosferatu = Nosferatu(invasion_settings, screen, bounty_hunter)
        nosferatus.add(new_nosferatu)

def detect_collisions(invasion_settings, game_stats, screen, bullets, 
    nosferatus, bounty_hunter, ammo_crates):

    if pygame.sprite.spritecollideany(bounty_hunter, nosferatus):
        #pygame.sprite.groupcollide(bounty_hunter, nosferatus, False, True)
        bounty_hunter_hit(invasion_settings, game_stats, screen, 
            bounty_hunter, nosferatus, bullets)

    # Detect collisions between bullets and enemies. 
    # Delete both if collision detected, and add 1 to player's score
    collisions = pygame.sprite.groupcollide(bullets, nosferatus, True, True)

    if collisions:
        game_stats.score += 1

    if pygame.sprite.spritecollideany(bounty_hunter, ammo_crates):
        collect_ammo(invasion_settings, screen, game_stats, ammo_crates)

def bounty_hunter_hit(invasion_settings, game_stats, screen, 
    bounty_hunter, nosferatus, bullets):

    game_stats.lives -= 1
    nosferatus.empty()
    bullets.empty()
    print(str(game_stats.lives))
    invasion_settings.ammo += 20

    if game_stats.lives == 0:
        nosferatus.empty()
        bullets.empty()
        sleep(1.5)
        game_stats.reset_stats()
        bounty_hunter.x = float(400)
        bounty_hunter.y = float(400)

def collect_ammo(invasion_settings, screen, game_stats, ammo_crates):
    
    invasion_settings.ammo += 21
    ammo_crates.empty()

def spawn_ammo_crate(invasion_settings, screen, game_stats, ammo_crates):

    if game_stats.game_active == True:
        new_ammo_crate = AmmoCrate(invasion_settings, screen, game_stats)
        ammo_crates.add(new_ammo_crate)

def level_up(invasion_settings, screen, game_stats):

    invasion_settings.nosferatu_spawnfactor = 5 + (invasion_settings.level * 0.2)
    invasion_settings.nosferatu_speedfactor = 1.5 + (invasion_settings.level * 0.05)
        
