import time
import numpy as np


def fill_grid(grid):
    moves = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    todo = {(0, 0, 0)}
    while len(todo) > 0:
        next = np.array(todo.pop())
        grid[tuple(next)] = 1
        for i, move in enumerate(moves):
            prev = tuple(next - move)
            fut = tuple(next + move)
            if next[i] > 0 and grid[prev] == 0:
                todo.add(prev)
            if next[i] < len(grid) - 1 and grid[fut] == 0:
                todo.add(fut)
    return grid


def count_free_faces(grid):
    a = np.vstack([z, grid[:-1]])
    b = np.vstack([grid[1:], z])
    c = np.vstack([z, grid.transpose((1, 0, 2))[:-1]]).transpose((1, 0, 2))
    d = np.vstack([grid.transpose((1, 0, 2))[1:], z]).transpose((1, 0, 2))
    e = np.vstack([z, grid.transpose((2, 1, 0))[:-1]]).transpose((2, 1, 0))
    f = np.vstack([grid.transpose((2, 1, 0))[1:], z]).transpose((2, 1, 0))

    adjacent_cubes = a + b + c + d + e + f
    free_sides = (6 - adjacent_cubes) * grid
    print(np.sum(free_sides))


with open("day18/input") as file:
    start = time.time()
    coords = [[int(n) for n in line.split(",")] for line in file.readlines()]
    coords = np.array(coords)
    width = np.max(coords) + 1
    grid = np.zeros((width, width, width))
    for x, y, z in coords:
        grid[x, y, z] = 1
    z = np.zeros((1, width, width))

    filled_grid = fill_grid(np.copy(grid))
    count_free_faces(1 - filled_grid + grid)
    print(int(time.time() - start))
