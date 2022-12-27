import time
import math


with open("day24/input.txt") as file:
    start = time.time()

    lines = file.readlines()
    height, width = len(lines) - 2, len(lines[0].strip()) - 2
    cycle_length = math.lcm(height, width)
    cyclone_positions = []
    cyclones_init = dict()

    # Parsing position and direction of all cyclones
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            match char:
                case ">":
                    cyclones_init[(r - 1, c - 1)] = (0, 1)
                case "<":
                    cyclones_init[(r - 1, c - 1)] = (0, -1)
                case "^":
                    cyclones_init[(r - 1, c - 1)] = (-1, 0)
                case "v":
                    cyclones_init[(r - 1, c - 1)] = (1, 0)

    # Calculating all cyclones positions through times (it cycles)
    for i in range(cycle_length):
        cyclone_positions_time_i = set()
        for (r, c), (r_mov, c_mov) in cyclones_init.items():
            cyclone_positions_time_i.add(
                ((r + r_mov * i) % height, (c + c_mov * i) % width)
            )
        cyclone_positions.append(cyclone_positions_time_i)

    # Getting all free positions through time instead during a cycle
    free_positions = []
    for i in range(cycle_length):
        free_positions_time_i = {(-1, 0), (height, width - 1)}
        cyclone_positions_time_i = cyclone_positions[i]
        for r in range(height):
            for c in range(width):
                if not (r, c) in cyclone_positions_time_i:
                    free_positions_time_i.add((r, c))
        free_positions.append(free_positions_time_i)
    # We get new graph with nodes ids being (r, c, time)
    # Edges exists iff t + 1 == t' and adjacent(p, p') and p' is in free_positions[t' % cycle_length]

    # BFS from departure at time 0.
    discovered = {(-1, 0, 0)}
    queue = [(-1, 0, 0)]
    min_time = None
    while len(queue) > 0:
        r, c, t = queue.pop(0)
        # When come across arrival, it must be the lowest time by bfs property (time coordinate always increases in queue) so stop and print result
        if r == height and c == width - 1:
            print(f"Takes minimum {t} steps")
            break

        potential_neighbors = [
            (r, c, t + 1),
            (r - 1, c, t + 1),
            (r + 1, c, t + 1),
            (r, c - 1, t + 1),
            (r, c + 1, t + 1),
        ]
        for (new_r, new_c, new_t) in potential_neighbors:
            if (new_r, new_c) in free_positions[new_t % cycle_length] and (
                new_r,
                new_c,
                new_t % cycle_length,
            ) not in discovered:
                discovered.add((new_r, new_c, new_t % cycle_length))
                queue.append((new_r, new_c, new_t))

    print(f"Ran in {int(time.time() - start)}s")
