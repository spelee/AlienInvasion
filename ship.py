import pygame

class Ship():

    def __init__(self, ai_settings, screen, sideways=False):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.sideways = sideways

        #Load the ship image and get is rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        if self.sideways:
            self.rect.left = self.screen_rect.left
            self.rect.centery = self.screen_rect.centery
        else:
            # Start each new ship at the bottom scenter of the screen.
            self.rect.centerx = self.screen_rect.centerx
            self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on the movement flag."""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def move_left(self, toggle):
        if self.ai_settings.horizontal_movements_permitted and toggle:
            self.moving_left = True
        else:
            self.moving_left = False

    def move_right(self, toggle):
        if self.ai_settings.horizontal_movements_permitted and toggle:
            self.moving_right = True
        else:
            self.moving_right = False

    def move_up(self, toggle):
        if self.ai_settings.vertical_movements_permitted and toggle:
            self.moving_up = True
        else:
            self.moving_up = False

    def move_down(self, toggle):
        if self.ai_settings.vertical_movements_permitted and toggle:
            self.moving_down = True
        else:
            self.moving_down = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)



