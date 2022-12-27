import numpy as np


def rotate_forest(forest, direction):
    if direction == 1:  # left
        forest = forest.transpose(0, 2, 1)[:, ::-1, :]
    if direction == 2:  # right
        forest = forest.transpose(0, 2, 1)
    if direction == 3:  # up
        forest = forest[:, ::-1, :]
    return forest


def unrotate_forest(forest, direction):
    if direction == 1:  # left
        forest = forest[:, ::-1, :].transpose(0, 2, 1)
    if direction == 2:  # right
        forest = forest.transpose(0, 2, 1)
    if direction == 3:  # up
        forest = forest[:, ::-1, :]
    return forest


def parse_forest(file):
    return np.array(
        list([list(map(lambda x: int(x), l.strip())) for l in file.readlines()])
    )


def make_scenic_score_map(forest, direction):
    # TODO : add a dimension of size 10 for each tree size and run with fixed size in every dimension
    forest = forest.copy()
    forest = np.repeat(forest[None, ...], 10, axis=0)
    forest = rotate_forest(forest, direction)

    for size in range(10):
        forest[size] = forest[size][::-1]
        for i in range(len(forest[size]) - 1):
            forest[size][i] = (size > forest[size][i + 1]) * 1
        forest[size] = forest[size][::-1]
        forest[size][0] = np.array([0] * len(forest[size][0]))

    for size in range(10):
        for i in range(len(forest[size]) - 1):
            forest[size][i + 1] = (forest[size][i] * forest[size][i + 1]) + 1
    forest = unrotate_forest(forest, direction)
    return forest


with open("day8/input") as file:
    forest = parse_forest(file)
    scenic_scores = []
    for i in range(4):
        scenic_scores.append(make_scenic_score_map(forest, i))
    total = scenic_scores[0] * scenic_scores[1] * scenic_scores[2] * scenic_scores[3]
    print(forest)
    mapped_total = forest.choose(total)
    print("final")
    print(mapped_total)
    print(np.max(mapped_total))
    index_top = np.unravel_index(np.argmax(mapped_total, axis=None), mapped_total.shape)
    print(index_top)
    print(forest[index_top])
