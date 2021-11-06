import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class for managing bullets"""

    def __init__(self, ai_game):
        """Create bullet in ship's position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Moving bullet on the screen"""
        self.y -= self.settings.bullet_speed

        self.rect.y = self.y

    def draw_bullet(self):
        """Display the bullet"""
        pygame.draw.rect(self.screen, self.color, self.rect)
