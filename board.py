import random
import numpy as np

from RandomMaze import random_maze
from constants import WHITE, RED, GREEN, BLUE, BLACK, MAZE_SIZE, VIEW_SIZE


class Board:

    def __init__(self):
        self.cell_size = 5
        self.row_len = MAZE_SIZE
        self.size = self.cell_size * self.row_len
        self.view_size = self.cell_size * VIEW_SIZE
        self.start_pos = (int(self.cell_size / 2), int(self.cell_size / 2))
        self.finish_pos = None
        self.im = None
        self.snake_pos = None
        self.old_snake_pos = None

    def init(self):
        maze = random_maze(self.row_len)
        self.im = np.array([WHITE] * self.size ** 2)
        self.im = np.reshape(self.im, (self.size, self.size, 3))
        self.snake_pos = self.start_pos
        self.old_snake_pos = self.snake_pos
        self.im[self.snake_pos] = GREEN
        self.finish_pos = (self.cell_size * random.randint(0, self.row_len - 1) + int(self.cell_size / 2),
                           self.cell_size * random.randint(0, self.row_len - 1) + int(self.cell_size / 2))
        self.im[self.finish_pos] = RED

        count = 0
        for row in maze:
            for cell in row:
                corner = (int(count / (self.size / self.cell_size)) * self.cell_size, int(count % (self.size / self.cell_size)) * self.cell_size)
                self.drow_cell(corner, cell)
                count += 1

    def drow_cell(self, corner, cell):
        if cell & 0x1:
            for i in range(self.cell_size):
                self.im[(corner[0], corner[1] + i)] = BLACK
        if cell & 0x2:
            for i in range(self.cell_size):
                self.im[(corner[0] + i, corner[1] + self.cell_size-1)] = BLACK
        if cell & 0x4:
            for i in range(self.cell_size):
                self.im[(corner[0] + self.cell_size-1, corner[1] + i)] = BLACK
        if cell & 0x8:
            for i in range(self.cell_size):
                self.im[(corner[0] + i, corner[1])] = BLACK
        if not (cell & 0x1 or cell & 0x2):
            self.im[(corner[0], corner[1] + self.cell_size - 1)] = BLACK
        if not (cell & 0x2 or cell & 0x4):
            self.im[(corner[0] + self.cell_size - 1, corner[1] + self.cell_size - 1)] = BLACK
        if not (cell & 0x4 or cell & 0x8):
            self.im[(corner[0] + self.cell_size - 1, corner[1])] = BLACK
        if not (cell & 0x8 or cell & 0x1):
            self.im[(corner[0], corner[1])] = BLACK

    def is_wall(self):
        poses = [(self.snake_pos[0] - 1 + i, self.snake_pos[1] - 1 + j)
                 for i in range(3) for j in range(3)]
        for pos in poses:
            if np.array_equal(self.im[pos], BLACK):
                return True
        return False

    def update(self):
        if self.is_wall():
            self.snake_pos = self.old_snake_pos
            return False
        self.im[self.old_snake_pos] = BLUE
        self.im[self.snake_pos] = GREEN
        self.old_snake_pos = self.snake_pos
        return True

    def is_finish_pos(self):
        return self.snake_pos == self.finish_pos

    def move_snake(self, y, x):
        self.snake_pos = ((self.snake_pos[0] + y) % self.size, (self.snake_pos[1] + x) % self.size)

    def clear(self):
        poses = [(i, j)
                 for i in range(self.size) for j in range(self.size)]
        for pos in poses:
            if np.array_equal(self.im[pos], BLUE):
                self.im[pos] = WHITE

    def is_clear(self, direction):
        if direction == 0:
            if np.array_equal(self.im[self.snake_pos[0] - int(self.cell_size / 2), self.snake_pos[1]], BLACK):
                return False
        elif direction == 1:
            if np.array_equal(self.im[self.snake_pos[0], self.snake_pos[1] + int(self.cell_size / 2)], BLACK):
                return False
        elif direction == 2:
            if np.array_equal(self.im[self.snake_pos[0] + int(self.cell_size / 2), self.snake_pos[1]], BLACK):
                return False
        elif direction == 3:
            if np.array_equal(self.im[self.snake_pos[0], self.snake_pos[1] - int(self.cell_size / 2)], BLACK):
                return False
        return True





