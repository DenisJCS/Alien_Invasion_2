class Settings():
    """Class for storing all settings of game Alien Invasion"""

    def __init__(self):
        """Initiated game settings"""
        #Parameters of screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
