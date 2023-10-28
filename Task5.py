# В этом коде я добавил метод visualize_grid_with_path(),
# который визуализирует сетку с помеченным путем передачи данных между башнями.

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

    def find_most_reliable_path(self, start_row, start_col, end_row, end_col):
        visited = [[False] * self.m for _ in range(self.n)]
        queue = [(start_row, start_col, 0)]
        min_transitions = float('inf')
        most_reliable_path = []

        while queue:
            row, col, transitions = queue.pop(0)
            visited[row][col] = True

            if row == end_row and col == end_col:
                if transitions < min_transitions:
                    min_transitions = transitions
                    most_reliable_path = [(row, col)]
                elif transitions == min_transitions:
                    most_reliable_path.append((row, col))

            for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_row, new_col = row + drow, col + dcol
                if 0 <= new_row < self.n and 0 <= new_col < self.m and self.grid[new_row][new_col] != 1 and not \
                        visited[new_row][new_col]:
                    queue.append((new_row, new_col, transitions + 1))

        return most_reliable_path, min_transitions

    def visualize_grid_with_path(self, path):
        plt.imshow(self.grid, cmap='Blues')

        for row, col in path:
            plt.text(col, row, 'X', ha='center', va='center', color='red', fontsize=10)

        plt.colorbar(ticks=[0, 1, 2, 3])
        plt.show()


# Пример использования:
grid = CityGrid(5, 7, 0.3)
grid.place_tower(1, 1, 2)
grid.place_tower(3, 5, 2)
path, transitions = grid.find_most_reliable_path(1, 1, 3, 5)
grid.visualize_grid_with_path(path)
