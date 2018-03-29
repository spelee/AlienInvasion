import sys

import pygame

from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right
        ship.move_right(True)
    elif event.key == pygame.K_LEFT:
        ship.move_left(True)
    elif event.key == pygame.K_UP:
        ship.move_up(True)
    elif event.key == pygame.K_DOWN:
        ship.move_down(True)
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings=ai_settings,
                    screen=screen, ship=ship, bullets=bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right(False)
    elif event.key == pygame.K_LEFT:
        ship.move_left(False)
    elif event.key == pygame.K_UP:
        ship.move_up(False)
    elif event.key == pygame.K_DOWN:
        ship.move_down(False)

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    # Set the background color
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    for b in bullets.sprites():
        b.draw_bullet()

    # Make the most recently draw screen visible
    pygame.display.flip()

def update_bullets(ai_settings, screen, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if not ai_settings.sideways_shooter:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        else:
            if bullet.rect.left >= screen.get_rect().right:
                bullets.remove(bullet)

def get_num_aliens(ai_settings, screen, alien_width):
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, alien_number, alien_width):
    alien = Alien(ai_settings, screen, ai_settings.sideways_shooter)
    alien.x = (alien_number * 2 * alien_width) + alien_width
    alien.rect.x = alien.x
    return alien


def create_fleet(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen, ai_settings.sideways_shooter)
    number_aliens_x = get_num_aliens(ai_settings, screen, alien.rect.width)

    for alien_number in range(number_aliens_x):
        alien = create_alien(ai_settings, screen, alien_number,
                             alien.rect.width)
        aliens.add(alien)



