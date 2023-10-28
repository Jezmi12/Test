# В этом коде я добавил метод optimize_tower_placement(),
# который размещает башни радиусом radius
# для каждого свободного блока сетки. Мы можем заменить вызов optimize_tower_placement()
# на любое другое значение радиуса.
# Далее я визуализирую сетку с помощью метода visualize_grid().

import random
import matplotlib.pyplot as plt


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

    def place_tower(self, row, col, radius):
        self.grid[row][col] = 2

        for i in range(max(0, row - radius), min(self.n, row + radius + 1)):
            for j in range(max(0, col - radius), min(self.m, col + radius + 1)):
                if abs(i - row) + abs(j - col) <= radius and self.grid[i][j] == 0:
                    self.grid[i][j] = 3

    def visualize_grid(self):
        plt.imshow(self.grid, cmap='Blues')
        plt.colorbar(ticks=[0, 1, 2, 3])
        plt.show()

    def optimize_tower_placement(self, radius):
        for row in range(self.n):
            for col in range(self.m):
                if self.grid[row][col] == 0:
                    self.place_tower(row, col, radius)


# Пример использования:
grid = CityGrid(5, 7, 0.3)
grid.optimize_tower_placement(2)  # размещаем башни с радиусом действия 2 для каждого свободного блока
grid.visualize_grid()
