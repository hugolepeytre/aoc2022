import numpy as np
import re


def simulate_cycle(inventories, activities, instructions):
    for i in range(len(inventories)):
        activities[i] += len(inventories[i])
        while len(inventories[i]) > 0:
            item = inventories[i].pop(0)
            item = instructions[i][0](item) // 3
            target = (
                instructions[i][2]
                if (item % instructions[i][1]) == 0
                else instructions[i][3]
            )
            inventories[target].append(item)
    return inventories, activities


with open("day11/input") as file:
    starts = file.read().split("\n\n")
    monkey_inventories = []
    monkey_activities = []
    monkey_instructions = []
    for start in starts:
        start = start.split("\n")
        monkey_activities.append(0)
        monkey_inventories.append(
            list(map(lambda x: int(x), re.findall(r"\d+", start[1])))
        )
        monkey_function = eval("lambda old: " + start[2].split("=")[-1])
        monkey_divisor = int(start[3].split()[-1])
        monkey_target_true = int(start[4].split()[-1])
        monkey_target_false = int(start[5].split()[-1])
        monkey_instructions.append(
            [monkey_function, monkey_divisor, monkey_target_true, monkey_target_false]
        )
    monkey_activities = np.array(monkey_activities)
    for i in range(20):
        monkey_inventories, monkey_activities = simulate_cycle(
            monkey_inventories, monkey_activities, monkey_instructions
        )
    tmp = np.partition(-monkey_activities, 2)
    print(-tmp[:2])
    print(tmp[0] * tmp[1])
