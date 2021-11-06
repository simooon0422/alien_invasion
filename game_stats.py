class GameStats:
    """Monitoring statistic data of the game"""

    def __init__(self, ai_game):
        """Initialization of statistic data"""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        self.high_score = 0

    def reset_stats(self):
        """Initialization of data that can be changed during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
