import time
import numpy as np


with open("day18/input") as file:
    start = time.time()
    coords = [[int(n) for n in line.split(",")] for line in file.readlines()]
    coords = np.array(coords)
    width = np.max(coords) + 1
    print(width)
    grid = np.zeros((width, width, width))
    for x, y, z in coords:
        grid[x, y, z] = 1
    z = np.zeros((1, width, width))

    a = np.vstack([z, grid[:-1]])
    b = np.vstack([grid[1:], z])
    c = np.vstack([z, grid.transpose((1, 0, 2))[:-1]]).transpose((1, 0, 2))
    d = np.vstack([grid.transpose((1, 0, 2))[1:], z]).transpose((1, 0, 2))
    e = np.vstack([z, grid.transpose((2, 1, 0))[:-1]]).transpose((2, 1, 0))
    f = np.vstack([grid.transpose((2, 1, 0))[1:], z]).transpose((2, 1, 0))

    adjacent_cubes = a + b + c + d + e + f
    free_sides = (6 - adjacent_cubes) * grid
    print(np.sum(free_sides))
    print(int(time.time() - start))
