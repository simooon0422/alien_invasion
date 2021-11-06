import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class for managing space ship"""

    def __init__(self, ai_game):
        """Initialize the space ship and its starting position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.screen_rect = ai_game.screen.get_rect()

        # Loading the image of the space ship and its rectangle
        self.image = pygame.image.load("images/ship.bmp").convert()
        self.image.set_colorkey((230, 230, 230))
        self.rect = self.image.get_rect()

        # Each new ship starts at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Convert ship's position to float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Ship moves
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update position of the ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Convert ship's position back to int
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Display the space ship in its recent position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
