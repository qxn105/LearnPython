class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self) -> None:
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.fullscreen_mode = 1
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #self.bg_color = (0, 0, 100)
        # Настройки корабля
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
