import time
import re


def numbers(string):
    return list([int(x) for x in re.findall(r"-?\d+", string)])


def letters(string):
    return list([x for x in re.findall(r"[a-zA-Z]", string)])


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
    og_r = r
    og_c = c
    r_incr = abs(r_shift) // r_shift if r_shift != 0 else 0
    c_incr = abs(c_shift) // c_shift if c_shift != 0 else 0
    counter = abs(r_shift) + abs(c_shift)
    new_d = d
    print(counter)
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
            print("found type 1")
            new_d = (new_d + 1) % 4 if r_incr != 0 else (new_d - 1) % 4
            r_incr, c_incr = -c_incr, -r_incr
        if maze[r][c] == 4:
            print("found type 2")
            new_d = (new_d - 1) % 4 if r_incr != 0 else (new_d + 1) % 4
            r_incr, c_incr = c_incr, r_incr
        r += r_incr
        c += c_incr
    print(f"From ({og_r}, {og_c}) dir {d}")
    print(f"To ({r}, {c}) dir {new_d}")
    return r, c, new_d


with open("day22/smol_input") as file:
    start = time.time()
    # Constants
    cube_width = 4
    init_row = 1 * cube_width
    init_col = 4 * cube_width
    init_dir = 0
    n_cubes_height = 6
    n_cubes_width = 7
    maze_width = n_cubes_width * cube_width
    maze_height = n_cubes_height * cube_width
    input_rows_shift = 1 * cube_width
    input_cols_shift = 2 * cube_width
    type_1_faces_coords = [(0, 2), (1, 3), (2, 1), (3, 6), (4, 4), (5, 5)]
    type_2_faces_coords = [(0, 4), (1, 6), (2, 5), (3, 3), (4, 2), (5, 1)]

    # Making maze
    maze_desc, instructions = file.read().split("\n\n")
    maze = [[2] * maze_width for _ in range(maze_height)]
    for r, line in enumerate(maze_desc.split("\n")):
        for c, char in enumerate(line):
            if char == ".":
                maze[r + input_rows_shift][c + input_cols_shift] = 0
            if char == "#":
                maze[r + input_rows_shift][c + input_cols_shift] = 1
    for (cube_r, cube_c) in type_1_faces_coords:
        for x in range(cube_width):
            maze[cube_r * cube_width + x][cube_c * cube_width + x] = 3
    for (cube_r, cube_c) in type_2_faces_coords:
        for x in range(cube_width):
            maze[cube_r * cube_width + cube_width - 1 - x][cube_c * cube_width + x] = 4

    # Initialization and instruction parsing
    r, c, d = init_row, init_col, init_dir
    turning_instrs = letters(instructions)
    moving_instrs = numbers(instructions)

    # Moving around
    r_shift, c_shift = get_shifts(d, moving_instrs[0])
    r, c, d = move(r, c, d, r_shift, c_shift, maze)
    for turning_instr, moving_instr in zip(turning_instrs, moving_instrs[1:]):
        d = turn(d, turning_instr)
        r_shift, c_shift = get_shifts(d, moving_instr)
        r, c, d = move(r, c, d, r_shift, c_shift, maze)

    # Result output
    print(
        "Result is",
        1000 * (r + 1 - input_rows_shift) + 4 * (c + 1 - input_cols_shift) + d,
    )
    print(f"Ran in {int(time.time() - start)}s")
