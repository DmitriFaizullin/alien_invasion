class GameStats():
    """Отслеживание статистики для игры Alien Invasion"""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в активном состоянии.
        self.game_active = False

        # Рекорд загружается из файла
        with open("high_score.txt") as file:
            self.high_score = int(file.read())

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        with open("high_score.txt", 'w') as file:
            file.write(str(self.high_score))

