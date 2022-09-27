import os
import pygame
from pygame.sprite import Sprite

dir = os.path.dirname(__file__) + '/'

class Alien(Sprite):
    """Класс, представляющий одного пришельца."""
    def __init__(self, ai_game) -> None:
        """Инициализирует пришельца и задает его начальную позицию."""
        super().__init__()
        self.screen = ai_game.screen
        # Загрузка изображения пришельца и назначение атрибута rect.
        self.image = pygame.image.load(dir+"images/alien.bmp")
        self.rect = self.image.get_rect()
        # Каждый новый пришелец появляется в левом верхнем углу экрана.
        # слева от него добавляется интервал, равный ширине пришельца, а над 
        # ним — интервал, равный высоте
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной горизонтальной позиции пришельца.
        self.x = float(self.rect.x)

    