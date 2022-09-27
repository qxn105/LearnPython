import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self) -> None:
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()
        if self.settings.fullscreen_mode: 
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()    

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = 1
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = 1 

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = 0 
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = 0 

    def  _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                sys.exit()
            elif  event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif  event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) >= self.settings.bullets_allowed:
            return
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Расчет позиции группы спрайтов пуль
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets  ))

    def  _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        # Назначение цвета фона.
        self.screen.fill(self.settings.bg_color)
        # Вывод корабля на экран
        self.ship.blitme()
        # Выводим пули на экран
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
        
    def run_gsme(self) -> None:
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_gsme()