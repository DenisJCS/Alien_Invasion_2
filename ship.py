import pygame

class Ship():
    """Class for ruling the ship"""
    def __init__(self, ai_game):
        """Initialize ship and sets it start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loading ship image and get rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Flag of moving
        self.moving_right = False

    def update(self):
        """Update ship's position from flag"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        """Draw ship in present postition"""
        self.screen.blit(self.image, self.rect)

