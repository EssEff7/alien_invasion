class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initializes statistics"""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # Initialize condition in which to display user entry for high score
        self.game_over = False
        
        # Read high score file to check for score or display a 0 
        try:
            filename = 'high_score.txt'
            with open(filename) as file_object:
                self.high_score = int(file_object.read())

        except FileNotFoundError:
            self.high_score = 0
        except ValueError:
            self.high_score = 0
            
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        