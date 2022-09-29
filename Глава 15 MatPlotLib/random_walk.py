from random import choice

class RandomWalk():
    """Класс для генерирования случайных блужданий."""
    def __init__(self, numpoints=5000) -> None:
        self.num_points = numpoints
        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]    
        self.y_values = [0]    
    
    def _get_step(self):
        direction = choice([1, -1])
        distance = choice(list(range(9)))
        return direction * distance
            

    def fill_walk(self):
        """Вычисляет все точки блуждания."""
        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:
            # Определение направления и длины перемещения.
            x_step = self._get_step()
            y_step = self._get_step()
            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue
            # Вычисление очередных значений x и y.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            # добавление значений в список
            self.x_values.append(x)
            self.y_values.append(y)