import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(ai_settings=ai_settings, screen=screen,
                sideways=ai_settings.sideways_shooter)
    bullets = Group()

    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)

    # Start the main loop for the game.
    while True:
        #Watch for keyboard and mouse events.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()
