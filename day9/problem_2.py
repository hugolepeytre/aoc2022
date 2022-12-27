import numpy as np


def move(front_position, back_position):
    relative_position = back_position - front_position
    if abs(relative_position[0]) == 2 or abs(relative_position[1]) == 2:
        relative_position = (abs(relative_position) // 2) * np.sign(relative_position)
    return front_position + relative_position


def move_head(head_position, direction):
    match direction:
        case "U":
            head_position += np.array([0, 1])
        case "D":
            head_position += np.array([0, -1])
        case "L":
            head_position += np.array([-1, 0])
        case "R":
            head_position += np.array([1, 0])
    return head_position


def move_all(positions, direction):
    positions[0] = move_head(positions[0], direction)
    for i in range(len(positions) - 1):
        positions[i + 1] = move(positions[i], positions[i + 1])
    return positions


with open("day9/input") as file:
    coordinates = []
    positions = [np.array([0, 0])] * 10
    for line in file.readlines():
        direction, repeat = line.split()
        repeat = int(repeat)
        for _ in range(repeat):
            positions = move_all(positions, direction)
            coordinates.append(positions[-1])
    final_set = set([(coords[0], coords[1]) for coords in coordinates])
    print(len(final_set))
