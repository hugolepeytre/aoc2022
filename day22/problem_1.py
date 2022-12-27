import time
import re


def numbers(string):
    return list([int(x) for x in re.findall(r"-?\d+", string)])


def letters(string):
    return list([x for x in re.findall(r"[a-zA-Z]", string)])


def dir_from_incrs(r_incr, c_incr):
    return (1 - c_incr) * abs(c_incr) + (2 - r_incr) * abs(r_incr)


def turn(d, turning_instr):
    if turning_instr == "R":
        return (d + 1) % 4
    if turning_instr == "L":
        return (d - 1) % 4


def get_shifts(d, moving_instr):
    c_shift = moving_instr * ((d % 2 == 0) * (1 - d))
    r_shift = moving_instr * ((d % 2 == 1) * (2 - d))
    return r_shift, c_shift


def move(r, c, d, r_shift, c_shift, maze):
    r_incr = abs(r_shift) // r_shift if r_shift != 0 else 0
    c_incr = abs(c_shift) // c_shift if c_shift != 0 else 0
    counter = abs(r_shift) + abs(c_shift)
    w = len(maze[0])
    h = len(maze)
    new_d = d
    while counter > 0 or maze[r][c] != 0:
        if maze[r][c] == 0:
            counter -= 1
        if maze[r][c] == 1:
            r_incr = -r_incr
            c_incr = -c_incr
            counter = 0
        if maze[r][c] == 2:
            pass
        if maze[r][c] == 3:
            r_incr, c_incr = c_incr, r_incr
            new_d = (new_d + 1) % 4 if r_incr != 0 else (new_d - 1) % 4
        if maze[r][c] == 4:
            r_incr, c_incr = -c_incr, -r_incr
            new_d = (new_d - 1) % 4 if r_incr != 0 else (new_d + 1) % 4
        r = (r + r_incr) % h
        c = (c + c_incr) % w
    return r, c, new_d


strings = []
with open("day22/input") as file:
    start = time.time()

    # Making maze
    maze_desc, instructions = file.read().split("\n\n")
    maze_dims = [len(l) for l in maze_desc.split("\n")]
    maze_height = len(maze_dims)
    maze_width = max(maze_dims)
    maze = [[2] * maze_width for _ in range(maze_height)]
    for r, line in enumerate(maze_desc.split("\n")):
        for c, char in enumerate(line):
            if char == ".":
                maze[r][c] = 0
            if char == "#":
                maze[r][c] = 1

    # Initialization and instruction parsing
    r, c, d = 0, 0, 0
    turning_instrs = letters(instructions)
    moving_instrs = numbers(instructions)
    r, c, d = move(r, c, d, 0, 1, maze)
    r, c, d = move(r, c, d, 0, -1, maze)

    # Moving around
    r_shift, c_shift = get_shifts(d, moving_instrs[0])
    r, c, d = move(r, c, d, r_shift, c_shift, maze)
    i = 0
    for turning_instr, moving_instr in zip(turning_instrs, moving_instrs[1:]):
        strings.append(f"({r}, {c})\n")
        d = turn(d, turning_instr)
        r_shift, c_shift = get_shifts(d, moving_instr)
        r, c, d = move(r, c, d, r_shift, c_shift, maze)
    print(r, c, d)
    print(1000 * (r + 1) + 4 * (c + 1) + d)
    print(f"Ran in {int(time.time() - start)}s")

with open("day22/output", "w+") as outfile:
    for s in strings:
        outfile.write(s)
