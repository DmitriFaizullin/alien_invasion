import pygame


class Ship():
    """Класс для управления кораблем."""

    def __init__(self, ai_game):  # получает ссылку на текущий экземпляр класса AlienInvasion
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen  # экран присваивается переменной
        self.screen_rect = ai_game.screen.get_rect()  # обращение к атрибуту rect экрана

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('images/ship.bmp')  # загрузка изображения корабля
        self.rect = self.image.get_rect()  # при работе с атрибутом rect доступны координаты сторон и центра
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom  # прямоугольник корабля выравнивается по атрибуту midbottom прямоугольника экрана

    def blitme(self):
        self.screen.blit(self.image, self.rect)  # метод выводит изображение на экран в позиции self.rect
