import re


def parse_initial_state(initial_state):
    lines = initial_state.split("\n")
    n_columns = int(lines[-1].split()[-1])
    stacks = [[] for _ in range(n_columns)]
    for line in lines[-2::-1]:
        for i in range(n_columns):
            crate = line[1 + (4 * i)]
            if crate != " ":
                stacks[i].append(crate)
    return stacks


def simulate(stacks, instructions):
    for instruction in instructions.split("\n"):
        print(instruction)
        n, stack_from, stack_to = map(lambda x: int(x), re.findall(r"\d+", instruction))
        removed_crates = stacks[stack_from - 1][-n:]
        remaining_crates = len(stacks[stack_from - 1]) - n
        stacks[stack_from - 1] = stacks[stack_from - 1][:remaining_crates]
        stacks[stack_to - 1] += removed_crates
    return stacks


with open("day5/input.txt") as file:
    initial_state, instructions = file.read().split("\n\n")
    stacks = parse_initial_state(initial_state)
    stacks = simulate(stacks, instructions)
    result = ""
    for s in stacks:
        result += s.pop()
    print(result)
