import numpy as np


with open("day10/input") as file:
    score = 0
    x = 1
    cycles = 1
    target_cycle_id = 0
    target_cycles = np.arange(6) * 40 + 20
    for line in file.readlines():
        cycles += 1
        if cycles >= target_cycles[target_cycle_id]:
            score += target_cycles[target_cycle_id] * x
            print(x, target_cycles[target_cycle_id], score)
            target_cycle_id += 1
            if target_cycle_id == len(target_cycles):
                print(score)
                exit()
        if line == "noop\n":
            pass
        else:
            _, val = line.split()
            x += int(val)
            cycles += 1
