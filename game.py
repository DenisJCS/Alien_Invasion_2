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
            self.check_event()
            self.ship.update()
            self.update_screen()
        # Redraw screen in every cicle

    def _check_events(self):
        """Реагирует на нажатие клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
    
    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _update_screen(self):
            #Every past cicle will draw it 
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Showing last drowned screen
            pygame.display.flip()

if __name__ == '__main__':
    # Creating expamle and run the game
    ai = AlienInvasion()
    ai.run_game()
