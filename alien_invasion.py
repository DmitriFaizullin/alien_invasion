import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()  # инициализирует настройки
        self.settings = Settings()  # настройки - класс Settings из файла settings

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))  # создание окна
        pygame.display.set_caption("Alien Invasion")  # заголовок окна
        self.ship = Ship(self)  # создается экземпляр класса Ship, ему передается текущий экран

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()  # проверить события
            self.ship.update()  # изменение положения коробля
            self._update_screen()  # отобразить новый экран

    def _check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():  # Отслеживание событий клавиатуры и мыши.
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # нажата кнопка клавиатуры
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:  # отпущена кнопка клавиатуры
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:  # нажата кнопка вправо
            # Переместить корабль вправо.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # нажата кнопка влево
            # Переместить корабль влево.
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """Реагирует на отпускание клавиш"""
        if event.key == pygame.K_RIGHT:  # отпущена кнопка вправо
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # отпущена кнопка влево
            self.ship.moving_left = False

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)  # экран заполняется цветом фона
        self.ship.blitme()  # корабль рисуется на экране
        pygame.display.flip()  # Отображение последнего прорисованного экрана.


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
