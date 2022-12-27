import re

MAX_DIM = 4000000


def widen(ranges, new_range):
    if len(ranges) == 0:
        return [new_range]
    i = 0
    while i < len(ranges):
        if ranges[i][0] <= new_range[0] and new_range[0] <= ranges[i][1] + 1:
            old_range = ranges.pop(i)
            return widen(
                ranges,
                [min(new_range[0], old_range[0]), max(new_range[1], old_range[1])],
            )
        if ranges[i][0] > new_range[0] and new_range[1] >= ranges[i][0] - 1:
            old_range = ranges.pop(i)
            return widen(
                ranges,
                [min(new_range[0], old_range[0]), max(new_range[1], old_range[1])],
            )
        i += 1
    ranges.insert(i - 1, new_range)
    return ranges


def widen_dead_x(sensor_x, sensor_y, beacon_x, beacon_y, dead_x):
    dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    print(dist)
    for i in range(dist):
        width_dead_x = dist - i
        y_above = min(sensor_y + i - 1, MAX_DIM - 1)
        y_below = max(sensor_y - i - 1, 0)
        x_above = min(sensor_x + width_dead_x, MAX_DIM)
        x_below = max(sensor_x - width_dead_x, 0)
        dead_x[y_above] = widen(dead_x[y_above], [x_below, x_above])
        dead_x[y_below] = widen(dead_x[y_below], [x_below, x_above])
    return dead_x


with open("day15/input") as file:
    dead_x = [[] for _ in range(MAX_DIM)]
    for line in file.readlines():
        sensor_x, sensor_y, beacon_x, beacon_y = map(
            lambda x: int(x), re.findall(r"-?\d+", line)
        )
        dead_x = widen_dead_x(sensor_x, sensor_y, beacon_x, beacon_y, dead_x)
    for i, range in enumerate(dead_x):
        if len(range) > 1:
            print(i + 1, range)
        elif range[0][0] > 0 or range[0][1] < MAX_DIM:
            print(i + 1, range)
