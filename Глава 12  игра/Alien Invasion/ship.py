import os
import pygame
dir = os.path.dirname(__file__) + '/'

class Ship():
    """Класс для управления кораблем."""
    def __init__(self, ai_game) -> None:
        """Инициализирует корабль и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load(dir + 'images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
        # состояние движения корабля
        self.moving_right = 0
        self.moving_left = 0
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)
    
    def update(self):
        """Рисует корабль в текущей позиции."""
        # обновление текущей позиции
        # Обновляется атрибут x, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right: 
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:  
            self.x -= self.settings.ship_speed
        # Обновление атрибута rect на основании self.x.
        self.rect.x = self.x


    def blitme(self) -> None:
        # отрисовка
        self.screen.blit(self.image, self.rect)