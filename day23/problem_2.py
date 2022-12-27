import time


def add_proposition(elf, positions, first_considered, propositions):
    r, c = elf
    final_proposition = None
    acceptable_directions = 0
    for i in range(4):
        direction = (first_considered + i) % 4
        count_elves = 0
        for j in range(3):
            match direction:
                case 0:  # north
                    proposition = (r - 1, c)
                    if (r - 1, c - 1 + j) in positions:
                        count_elves += 1
                case 1:  # south
                    proposition = (r + 1, c)
                    if (r + 1, c - 1 + j) in positions:
                        count_elves += 1
                case 2:  # west
                    proposition = (r, c - 1)
                    if (r - 1 + j, c - 1) in positions:
                        count_elves += 1
                case 3:  # east
                    proposition = (r, c + 1)
                    if (r - 1 + j, c + 1) in positions:
                        count_elves += 1

        if count_elves == 0:
            acceptable_directions += 1
            if final_proposition is None:
                final_proposition = proposition
    if final_proposition is None or acceptable_directions == 4:
        final_proposition = elf
    if final_proposition in propositions:
        propositions[final_proposition].append(elf)
    else:
        propositions[final_proposition] = [elf]


def print_field(positions):
    min_r, min_c = 10000000000, 10000000000
    max_r, max_c = 0, 0
    for r, c in positions:
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)
    print(min_r, min_c)
    rectangle_height = max_r - min_r + 1
    rectangle_width = max_c - min_c + 1
    field = [["."] * rectangle_width for _ in range(rectangle_height)]
    for r, c in positions:
        field[r - min_r][c - min_c] = "#"
    for line in field:
        print("".join(line))
    print()


with open("day23/input") as file:
    start = time.time()
    positions = set()
    for r, line in enumerate(file.readlines()):
        for c, char in enumerate(line):
            if char == "#":
                positions.add((r, c))

    print(f"{len(positions)} elves at the beginning")
    propositions = dict()
    prev_positions = None
    first_considered = 0
    i = 0
    while prev_positions != positions:
        prev_positions = positions.copy()
        for elf in positions:
            add_proposition(elf, positions, first_considered, propositions)

        positions = set()
        for proposition, proposers in propositions.items():
            if len(proposers) == 1:
                positions.add(proposition)
            else:
                for proposer in proposers:
                    positions.add(proposer)
        propositions = dict()
        first_considered = (first_considered + 1) % 4
        i += 1

    min_r, min_c = 10000000000, 10000000000
    max_r, max_c = 0, 0
    for r, c in positions:
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)

    print(f"Did {i} iterations")
    print(f"Corners are ({min_r}, {min_c}), ({max_r}, {max_c}), {len(positions)} elves")
    rectangle_height = max_r - min_r + 1
    rectangle_width = max_c - min_c + 1
    print(f"{rectangle_height*rectangle_width - len(positions)} empty ground tiles")
    print(f"Ran in {int(time.time() - start)}s")
