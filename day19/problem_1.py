import time
import re


def quality_rec(
    dynamic, costs, max_costs, robots=(1, 0, 0), resources=(0, 0, 0), current_minute=0
):
    if current_minute >= 24:
        return 0
    remaining_building_steps = 23 - current_minute
    remaining_mining_steps = remaining_building_steps - 1
    for i in range(3):
        if (resources[i] + robots[i] * remaining_mining_steps) > (
            remaining_building_steps * max_costs[i]
        ):
            resources = fix_n_to_max(i, resources)

    if (robots, resources, current_minute) in dynamic:
        return dynamic[(robots, resources, current_minute)]

    new_robots = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)]
    sols = [0]
    for i, (cost, new_r) in enumerate(zip(costs, new_robots)):
        # checking if building has worth
        if i < 3 and resources[i] == 9999:
            continue

        # starting building target robot
        new_resources = sum_tuples(resources, cost)
        next_step = 1
        negative_index = neg_idx(new_resources)
        can_be_legal = True
        while negative_index is not None and can_be_legal:
            new_resources = sum_tuples(new_resources, robots)
            negative_index = neg_idx(new_resources)
            can_be_legal = (
                robots[negative_index] > 0 if negative_index is not None else True
            )
            next_step += 1
        new_resources = sum_tuples(new_resources, robots)
        robot_finish_time = current_minute + next_step
        added_score = 24 - robot_finish_time if sum(new_r) == 0 else 0
        new_resources = fix_to_max(new_resources)
        if negative_index is None and robot_finish_time <= 24:
            sols.append(
                added_score
                + quality_rec(
                    dynamic,
                    costs,
                    max_costs,
                    sum_tuples(robots, new_r),
                    new_resources,
                    robot_finish_time,
                )
            )

    best = max(sols)
    dynamic[(robots, resources, current_minute)] = best
    return best


def sum_tuples(t1, t2):
    return tuple([sum(x) for x in zip(t1, t2)])


def neg_idx(tup):
    for i, r in enumerate(tup):
        if r < 0:
            return i
    return None


def fix_to_max(tup):
    return tuple([9999 if x > 9000 else x for x in tup])


def fix_n_to_max(n, tup):
    return tuple([9999 if i == n else x for i, x in enumerate(tup)])


def quality(
    i,
    ore_ore,
    clay_ore,
    obs_ore,
    obs_clay,
    geode_ore,
    geode_obs,
):
    print("blueprint : ", i)
    dynamic = dict()
    costs = [
        (-ore_ore, 0, 0),
        (-clay_ore, 0, 0),
        (-obs_ore, -obs_clay, 0),
        (-geode_ore, 0, -geode_obs),
    ]
    max_costs = (max([ore_ore, clay_ore, obs_ore, geode_ore]), obs_clay, geode_obs)
    best_geodes = quality_rec(dynamic, costs, max_costs)
    print(best_geodes)
    return i * best_geodes


def numbers(string):
    return list([int(x) for x in re.findall(r"-?\d+", string)])


with open("day19/input") as file:
    start = time.time()
    qualities = [quality(*numbers(blueprint)) for blueprint in file.readlines()]
    print(qualities)
    print(sum(qualities))
    print(int(time.time() - start))
