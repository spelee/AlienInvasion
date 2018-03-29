import sys

import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen, sideways=False):
        """Initialize the alien and set its starting position."""
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings
        self.sideways = sideways

        #Load the image and get its rect.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        if self.sideways:
            #self.rect.left = self.screen_rect.left
            #self.rect.centery = self.screen_rect.centery
            sys.exit(1);
        else:
            # Start each at the top left of the screm
            #self.rect.left = self.screen_rect.left
            #self.rect.top = self.screen_rect.top
            self.rect.x = self.rect.width
            self.rect.y = self.rect.height

        # Store a decimal value for the ship's center.
        self.x = float(self.rect.x)
        #self.centery = float(self.rect.centery)

        # Movement flag
        """
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        """

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)



