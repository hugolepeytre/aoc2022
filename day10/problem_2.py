import numpy as np


def draw(crt, x, cycles):
    cycles = cycles - 1
    x_pos = cycles % 40
    if x - 1 <= x_pos and x_pos <= x + 1:
        crt[cycles // 40][x_pos] = "#"
    return crt


with open("day10/input") as file:
    score = 0
    x = 1
    cycles = 1
    crt = list([["."] * 40 for _ in range(6)])
    for line in file.readlines():
        cycles += 1
        crt = draw(crt, x, cycles)
        if not "noop" in line:
            _, val = line.split()
            x += int(val)
            cycles += 1
            draw(crt, x, cycles)
    for line in crt:
        print("".join(line))
