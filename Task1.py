# В этом коде я создаю класс CityGrid, который инициализирует сетку с заданными размерами n x m
# Заблокированные блоки размещаются случайным образом с покрытием obstacle_coverage.
# Метод print_grid() используется для визуализации сетки.

import random


class CityGrid:
    def __init__(self, n, m, obstacle_coverage):
        self.n = n
        self.m = m
        self.grid = [[0] * m for _ in range(n)]
        self.obstacle_coverage = obstacle_coverage
        self.place_obstacles()

    def place_obstacles(self):
        num_obstacles = int(self.n * self.m * self.obstacle_coverage)

        for _ in range(num_obstacles):
            row = random.randint(0, self.n - 1)
            col = random.randint(0, self.m - 1)
            self.grid[row][col] = 1

    def print_grid(self):
        for row in self.grid:
            print(' '.join(map(str, row)))


# Для смены параметров:
grid = CityGrid(5, 7, 0.3)
grid.print_grid()
