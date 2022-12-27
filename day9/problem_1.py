import numpy as np


def move(head_position, tail_position, direction):
    match direction:
        case "U":
            head_position += np.array([0, 1])
        case "D":
            head_position += np.array([0, -1])
        case "L":
            head_position += np.array([-1, 0])
        case "R":
            head_position += np.array([1, 0])

    relative_position = tail_position - head_position
    if abs(relative_position[0]) == 2 or abs(relative_position[1]) == 2:
        relative_position = (abs(relative_position) // 2) * np.sign(relative_position)
    return head_position + relative_position, head_position


with open("day9/input") as file:
    coordinates = []
    coordinates.append(np.array([0, 0]))
    head_position = np.array([0, 0])
    tail_position = np.array([0, 0])
    for line in file.readlines():
        direction, repeat = line.split()
        repeat = int(repeat)
        for _ in range(repeat):
            tail_coord, head_coord = move(head_position, tail_position, direction)
            head_position = head_coord
            tail_position = tail_coord
            coordinates.append(tail_position)
    final_set = set([(coords[0], coords[1]) for coords in coordinates])
    print(len(final_set))
