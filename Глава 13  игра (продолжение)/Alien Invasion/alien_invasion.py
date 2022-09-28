import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

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
        # Создание экземпляра для хранения игровой статистики.
        # и панели результатов.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        #
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()    
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        # Создание кнопки Play.
        self.play_button = Button(self, "Play")
    
    def _create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - alien_width
        available_space_y = (self.settings.screen_height - (3 * alien_height)
            - self.ship.rect.height)
        number_aliens_x = available_space_x // (2 * alien_width)
        number_aliens_y = available_space_y // (2 * alien_height)
        
        # Создание флота пришельцев.
        for alien_row in range(number_aliens_y):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, alien_row)
        
            

    def _create_alien(self, alien_number, alien_row):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien_height + 2 * alien_height * alien_row
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()
        if not self.stats.game_active:
            return
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
    
    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.stats.reset_stats()
            self.stats.game_active = True
            # Очистка списков пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()
            # Создание нового флота и размещение корабля в центре.
            self._create_fleet()
            self.ship.center_ship()
            # Указатель мыши скрывается.
            pygame.mouse.set_visible(False)
            # Сброс скорости на дефолтную
            # Сброс игровых настроек.
            self.settings.initialize_dynamic_settings()
            self.sb.prep_score()
            self.sb.prep_level()

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        # Уменьшение ships_left и обновление панели счета
        self.stats.ships_left -= 1
        self.sb.prep_ships()
        if not self.stats.ships_left:
            self.stats.game_active = False
            # Указатель мыши показать.
            pygame.mouse.set_visible(True)
            return
        # Очистка списков пришельцев и снарядов.
        self.aliens.empty()
        self.bullets.empty()
        # Создание нового флота и размещение корабля в центре.
        self._create_fleet()
        self.ship.center_ship()
        # Пауза.
        sleep(0.5)

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит то же, что при столкновении с кораблем.
                self._ship_hit()
                break

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if len(self.bullets) >= self.settings.bullets_allowed:
            return
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_bullet_alien_collisions(self):
        """Проверка попаданий в пришельцев."""
        # При обнаружении попадания удалить снаряд и пришельца.
        collisions = pygame.sprite.groupcollide(
                self.bullets, self.aliens, True, True)
        if collisions:
            for key in collisions:
                self.stats.score += len(collisions[key]) * self.settings.alien_points
            self.sb.prep_score()
            self.sb.check_high_score()
        # Восстановление флота (все сбиты)
        if not self.aliens:
            # Уничтожение существующих снарядов и создание нового флота.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            # Увеличение уровня.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Расчет позиции группы спрайтов пуль
        self.bullets.update()
        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        #print(len(self.bullets  ))
        self._check_bullet_alien_collisions()

    def  _check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Обновляет позиции всех пришельцев во флоте."""
        self._check_fleet_edges()
        self.aliens.update()
        # Проверка коллизий "пришелец — корабль".
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # Проверить, добрались ли пришельцы до нижнего края экрана.
        self._check_aliens_bottom()

    def  _update_screen(self):
        # При каждом проходе цикла перерисовывается экран.
        # Назначение цвета фона.
        self.screen.fill(self.settings.bg_color)
        # Вывод корабля на экран
        self.ship.blitme()
        # Выводим пули на экран
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Выводим пришельцев на экран
        self.aliens.draw(self.screen)
        # Вывод информации о счете.
        self.sb.show_score()
        # Кнопка Play отображается в том случае, если игра неактивна.
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
        
    def run_gsme(self) -> None:
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_gsme()