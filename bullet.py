import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position"""
        super().__init__()

        self.screen = screen
        self.sideways = ai_settings.sideways_shooter

        # create a bullet rect at (0, 0) and then set correct position
        if not self.sideways:
            self.rect = pygame.Rect(
                0,0, ai_settings.bullet_width, ai_settings.bullet_height)
            self.rect.centerx = ship.rect.centerx
            self.rect.top = ship.rect.top
        else:
            self.rect = pygame.Rect(
                0, 0, ai_settings.bullet_height, ai_settings.bullet_width)
            self.rect.right = ship.rect.right
            self.rect.centery = ship.rect.centery

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.centerx = float(self.rect.centerx)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""

        # Update the decimal position of the bullet
        if not self.sideways:
            self.y -= self.speed_factor
        else:
            self.centerx += self.speed_factor
        self.rect.y = self.y
        self.rect.centerx = self.centerx

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)