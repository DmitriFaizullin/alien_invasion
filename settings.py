class Settings():
    """Класс длдя хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (247, 247, 247)

        # Настройки корабля
        self.ship_speed = 1.5

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # fleet_direction = 1 обозначает движение вправо; a -1 - влево.
