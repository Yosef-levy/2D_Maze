import random

import numpy as np


def random_maze(size=5):
    maze = np.array([16] * size ** 2)
    maze = np.reshape(maze, (size, size))
    start = (random.randint(0, size-1), random.randint(0, size-1))
    count = 1
    walls = []
    append(walls, start, 4)
    maze[start] = 15
    while count < size**2:
        wall = random.choice(walls)
        walls.remove(wall)
        n = neighbor(wall)
        if n[0] < 0 or n[0] >= size or n[1] < 0 or n[1] >= size:
            continue
        if maze[n] < 16:
            continue
        maze[wall[0], wall[1]] -= 0x1 << wall[2]
        maze[n] = 15 - (0x1 << ((wall[2] + 2) % 4))
        append(walls, n, (wall[2] + 2) % 4)
        count += 1
    return maze


def append(walls, cell, direction):
    new_walls = [0, 1, 2, 3]
    if direction < 4:
        new_walls.remove(direction)
    for i in new_walls:
        walls.append((cell[0], cell[1], i))


def neighbor(wall):
    if wall[2] == 0:
        return wall[0] - 1, wall[1]
    if wall[2] == 1:
        return wall[0], wall[1] + 1
    if wall[2] == 2:
        return wall[0] + 1, wall[1]
    if wall[2] == 3:
        return wall[0], wall[1] - 1
