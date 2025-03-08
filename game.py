import sys 
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class for managing resources and game habits"""
    def __init__(self):
        """Initiate game and creates game resources"""
        pygame.init()
        self.settings = Settings()


        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.scree_height))
        pygame.display.set_caption("Aline Invasion")
        self.ship = Ship(self)

        # Setting background color
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """Run main cicle of game"""
        while True:
            # Tracking events of mouse and keyboard
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Every past cicle will draw it 
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Showing last drowned screen
            pygame.display.flip()

if __name__ == '__main__':
    # Creating expamle and run the game
    ai = AlienInvasion()
    ai.run_game()
