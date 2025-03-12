import pygame

class Ship():
    """Class for ruling the ship"""
    def __init__(self, ai_game):
        """Initialize ship and sets it start position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings 

        # Loading ship image and get rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Saving ships coordinats
        self.x = float(self.rect.x) 

        # Flag of moving
        self.moving_right = False
        self.moving_left = False 

    def update(self):
        """Update ship's position from flag"""
        # Updating atribut x, not rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # Updating rect atribut based on self.x
        self.rect.x = self.x 

    def blitme(self):
        """Draw ship in present postition"""
        self.screen.blit(self.image, self.rect)

