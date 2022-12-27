import time


def eval_monkey(monkey):
    return eval(instrs[monkey])


with open("day21/input") as file:
    start = time.time()
    instrs = dict()
    for line in file.readlines():
        monkey, instr = line.split(":")
        instr = instr.split()
        if len(instr) == 1:
            instrs[monkey] = instr[0]
        else:
            instrs[
                monkey
            ] = f"eval_monkey('{instr[0]}') {instr[1]} eval_monkey('{instr[2]}')"
    print(eval_monkey("root"))
    print(f"Ran in {int(time.time() - start)}s")
