import numpy as np


def rotate_forest(forest, direction):
    if direction == 1:  # left
        forest = forest.T[::-1]
    if direction == 2:  # right
        forest = forest.T
    if direction == 3:  # up
        forest = forest[::-1]
    return forest


def unrotate_forest(forest, direction):
    if direction == 1:  # left
        forest = forest[::-1].T
    if direction == 2:  # right
        forest = forest.T
    if direction == 3:  # up
        forest = forest[::-1]
    return forest


def parse_forest(file):
    return (
        np.array(
            list([list(map(lambda x: int(x), l.strip())) for l in file.readlines()])
        )
        + 1
    )


def make_visible_map(forest, direction):
    forest = forest.copy()
    forest = rotate_forest(forest, direction)
    for i in range(len(forest) - 1):
        indices_to_keep_low = (forest[i + 1] > forest[i]) * 1
        indices_to_keep_high = 1 - indices_to_keep_low
        forest[i + 1] = (
            forest[i] * indices_to_keep_high + forest[i + 1] * indices_to_keep_low
        )
    forest = forest[::-1]
    for i in range(len(forest) - 1):
        forest[i] -= forest[i + 1]
    forest = forest[::-1]
    forest = unrotate_forest(forest, direction)
    return forest


with open("day8/input") as file:
    forest = parse_forest(file)
    visible_maps = []
    for i in range(4):
        visible_maps.append(make_visible_map(forest, i))
    print(forest)
    for v in visible_maps:
        print(v)
    total = visible_maps[0] + visible_maps[1] + visible_maps[2] + visible_maps[3]
    print(np.count_nonzero(total))
