import numpy as np


def sand_straight_fall(grid, grain_x, grain_y):
    col = grid[grain_x]
    nonzeroes = np.flatnonzero(col[grain_y:])
    if len(nonzeroes) == 0:
        return None
    return nonzeroes[0] + grain_y - 1


def add_sand(grid, grain_x, grain_y):
    grain_y = sand_straight_fall(grid, grain_x, grain_y)
    if not grain_y:
        return None
    if grain_x == 0:
        return None
    if grid[grain_x - 1][grain_y + 1] == 0:
        return add_sand(grid, grain_x - 1, grain_y + 1)
    if grain_x == len(grid) + 1:
        return None
    if grid[grain_x + 1][grain_y + 1] == 0:
        return add_sand(grid, grain_x + 1, grain_y + 1)
    grid[grain_x, grain_y] = 1
    return grid


def add_rocks(current_x, current_y, new_x, new_y, rocks):
    if current_x != new_x:
        for i in range(abs(new_x - current_x) + 1):
            rocks.add((min(current_x, new_x) + i, current_y))
    if current_y != new_y:
        for i in range(abs(new_y - current_y) + 1):
            rocks.add((current_x, min(current_y, new_y) + i))
    return rocks


with open("day14/input") as file:
    sand_grains = 1
    min_x = 10000
    max_x = 0
    min_y = 0
    max_y = 0
    rocks = set([])
    for line in file.readlines():
        coords = line.split(" -> ")
        current_x, current_y = [int(x) for x in coords[0].split(",")]
        min_x = min(min_x, current_x)
        max_x = max(max_x, current_x)
        max_y = max(max_y, current_y)
        for coord in coords[1:]:
            new_x, new_y = [int(x) for x in coord.split(",")]
            rocks = add_rocks(current_x, current_y, new_x, new_y, rocks)
            current_x, current_y = new_x, new_y
            min_x = min(min_x, current_x)
            max_x = max(max_x, current_x)
            max_y = max(max_y, current_y)
    grid = np.zeros((max_x - min_x + 1, max_y + 1))
    origin_x = 500 - min_x
    for rock_x, rock_y in rocks:
        grid[rock_x - min_x, rock_y] = 1
    grid = add_sand(grid, origin_x, 0)
    while grid is not None:
        grid = add_sand(grid, origin_x, 0)
        sand_grains += 1
    print(sand_grains - 1)
