class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self) -> None:
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.fullscreen_mode = 0
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #self.bg_color = (0, 0, 100)
        # Настройки корабля
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 5
        self.bullet_width = 3000
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Темп ускорения игры
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        # Подсчет очков
        self.alien_points = 50
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = self.ship_speed
        self.bullet_speed_factor = self.bullet_speed
        self.alien_speed_factor = self.alien_speed
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)