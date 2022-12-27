import time


def eval_monkey(monkey):
    monkey_instr = instrs[monkey]
    if len(monkey_instr) == 1:
        if monkey_instr[0] == "x":
            return (1, 0, 1)
        return int(monkey_instr[0])
    part1 = eval_monkey(monkey_instr[0])
    part2 = eval_monkey(monkey_instr[2])
    op = monkey_instr[1]
    if isinstance(part1, int) and isinstance(part2, int):
        return int(eval(f"{part1}{op}{part2}"))
    if isinstance(part2, tuple):
        if op == "*":
            return (part2[0] * part1, part2[1] * part1, part2[2])
        if op == "+":
            return (part2[0], part2[1] + (part1 * part2[2]), part2[2])
        if op == "-":
            return (-part2[0], (part2[2] * part1) - part2[1], part2[2])
        if op == "/":
            print("wshh")
            return None
        if op == "==":
            print(f"({part2[0]}x + {part2[1]})/{part2[2]} == {part1}")
    if isinstance(part1, tuple):
        if op == "*":
            return (part1[0] * part2, part1[1] * part2, part1[2])
        if op == "+":
            return (part1[0], part1[1] + (part1[2] * part2), part1[2])
        if op == "-":
            return (part1[0], part1[1] - (part2 * part1[2]), part1[2])
        if op == "/":
            return (part1[0], part1[1], part1[2] * part2)
        if op == "==":
            print(f"({part1[0]}x + {part1[1]})/{part1[2]} == {part2}")
            print(f"x = {int((part2 * part1[2] - part1[1])/part1[0])}")
    else:
        print(type(part1), type(part2))


with open("day21/input_p2") as file:
    start = time.time()
    instrs = dict()
    for line in file.readlines():
        monkey, instr = line.split(":")
        instr = instr.split()
        instrs[monkey] = instr
    x = 0
    success = False
    computation = eval_monkey("root")
    print(f"Ran in {int(time.time() - start)}s")
