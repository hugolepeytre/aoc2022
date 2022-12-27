import re


def dead_zone_at_line(sensor_x, sensor_y, beacon_x, beacon_y, dead_line):
    dead_x = set()
    dist = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    width_dead_zone = (
        sensor_y - dead_line + dist
        if dead_line >= sensor_y
        else dead_line - sensor_y + dist
    )
    for i in range(width_dead_zone + 1):
        dead_x.add(sensor_x + i)
        dead_x.add(sensor_x - i)
    return dead_x


with open("day15/input") as file:
    dead_x = set()
    dead_line = 2000000
    beacons = set()
    for line in file.readlines():
        sensor_x, sensor_y, beacon_x, beacon_y = map(
            lambda x: int(x), re.findall(r"-?\d+", line)
        )
        if beacon_y == dead_line:
            beacons.add(beacon_x)
        dead_x = dead_x.union(
            dead_zone_at_line(sensor_x, sensor_y, beacon_x, beacon_y, dead_line)
        )
    print(len(dead_x - beacons))
