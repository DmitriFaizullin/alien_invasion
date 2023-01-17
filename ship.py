import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Класс для управления кораблем."""

    def __init__(self, ai_game):  # получает ссылку на текущий экземпляр класса AlienInvasion
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen  # экран присваивается переменной
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  # обращение к атрибуту rect экрана

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')  # загрузка изображения корабля
        self.rect = self.image.get_rect()  # при работе с атрибутом rect доступны координаты сторон и центра
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom  # прямоугольник корабля выравнивается по атрибуту midbottom прямоугольника экрана
        # Сохранение вещественной координаты центра корабля
        self.x = float(self.rect.x)
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Обновляет позицию корабля с учетом флага"""
        # Обновляется атрибут x, не rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x += -self.settings.ship_speed

        # Обновление атрибута rect на основании self.x
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # метод выводит изображение на экран в позиции self.rect

    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
