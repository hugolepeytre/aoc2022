import time


def simulate_fall(tunnel, gas, rock_type):
    rock_c = 2
    rock_r = len(tunnel) + 3
    while True:
        dir = gas[gas_shot[0] % len(gas)]
        gas_shot[0] += 1
        if dir == "<":
            rock_c, rock_r = push_left(rock_c, rock_r, rock_type, tunnel)
        if dir == ">":
            rock_c, rock_r = push_right(rock_c, rock_r, rock_type, tunnel)
        rock_c, rock_r, rest = fall(rock_c, rock_r, rock_type, tunnel)
        if rest:
            update_tunnel(rock_c, rock_r, rock_type, tunnel)
            return


def add_rock(rock_c, rock_r, tunnel):
    if rock_r >= len(tunnel):
        tunnel.append([0] * 7)
        add_rock(rock_c, rock_r, tunnel)
    else:
        tunnel[rock_r][rock_c] = 1


def check_collision(rock_c, rock_r, tunnel):
    if rock_c < 0 or rock_c > 6:
        return True
    if rock_r >= len(tunnel):
        return False
    return tunnel[rock_r][rock_c] == 1


def push_left(rock_c, rock_r, rock_type, tunnel):
    can_move = None
    match rock_type:
        case 0:
            can_move = not check_collision(rock_c - 1, rock_r, tunnel)
        case 1:
            can_move = not (
                check_collision(rock_c - 1, rock_r + 1, tunnel)
                or check_collision(rock_c, rock_r, tunnel)
                or check_collision(rock_c, rock_r + 2, tunnel)
            )
        case 2:
            can_move = not (
                check_collision(rock_c - 1, rock_r, tunnel)
                or check_collision(rock_c + 1, rock_r + 1, tunnel)
                or check_collision(rock_c + 1, rock_r + 2, tunnel)
            )
        case 3:
            can_move = not (
                check_collision(rock_c - 1, rock_r, tunnel)
                or check_collision(rock_c - 1, rock_r + 1, tunnel)
                or check_collision(rock_c - 1, rock_r + 2, tunnel)
                or check_collision(rock_c - 1, rock_r + 3, tunnel)
            )
        case 4:
            can_move = not (
                check_collision(rock_c - 1, rock_r, tunnel)
                or check_collision(rock_c - 1, rock_r + 1, tunnel)
            )
    return (rock_c - 1, rock_r) if can_move else (rock_c, rock_r)


def push_right(rock_c, rock_r, rock_type, tunnel):
    can_move = None
    match rock_type:
        case 0:
            can_move = not check_collision(rock_c + 4, rock_r, tunnel)
        case 1:
            can_move = not (
                check_collision(rock_c + 3, rock_r + 1, tunnel)
                or check_collision(rock_c + 2, rock_r, tunnel)
                or check_collision(rock_c + 2, rock_r + 2, tunnel)
            )
        case 2:
            can_move = not (
                check_collision(rock_c + 3, rock_r, tunnel)
                or check_collision(rock_c + 3, rock_r + 1, tunnel)
                or check_collision(rock_c + 3, rock_r + 2, tunnel)
            )
        case 3:
            can_move = not (
                check_collision(rock_c + 1, rock_r, tunnel)
                or check_collision(rock_c + 1, rock_r + 1, tunnel)
                or check_collision(rock_c + 1, rock_r + 2, tunnel)
                or check_collision(rock_c + 1, rock_r + 3, tunnel)
            )
        case 4:
            can_move = not (
                check_collision(rock_c + 2, rock_r, tunnel)
                or check_collision(rock_c + 2, rock_r + 1, tunnel)
            )
    return (rock_c + 1, rock_r) if can_move else (rock_c, rock_r)


def fall(rock_c, rock_r, rock_type, tunnel):
    can_move = None
    match rock_type:
        case 0:
            can_move = not (
                check_collision(rock_c, rock_r - 1, tunnel)
                or check_collision(rock_c + 1, rock_r - 1, tunnel)
                or check_collision(rock_c + 2, rock_r - 1, tunnel)
                or check_collision(rock_c + 3, rock_r - 1, tunnel)
            )
        case 1:
            can_move = not (
                check_collision(rock_c, rock_r, tunnel)
                or check_collision(rock_c + 1, rock_r - 1, tunnel)
                or check_collision(rock_c + 2, rock_r, tunnel)
            )
        case 2:
            can_move = not (
                check_collision(rock_c, rock_r - 1, tunnel)
                or check_collision(rock_c + 1, rock_r - 1, tunnel)
                or check_collision(rock_c + 2, rock_r - 1, tunnel)
            )
        case 3:
            can_move = not check_collision(rock_c, rock_r - 1, tunnel)
        case 4:
            can_move = not (
                check_collision(rock_c, rock_r - 1, tunnel)
                or check_collision(rock_c + 1, rock_r - 1, tunnel)
            )
    return (rock_c, rock_r - 1, False) if can_move else (rock_c, rock_r, True)


def update_tunnel(rock_c, rock_r, rock_type, tunnel):
    match rock_type:
        case 0:
            add_rock(rock_c, rock_r, tunnel)
            add_rock(rock_c + 1, rock_r, tunnel)
            add_rock(rock_c + 2, rock_r, tunnel)
            add_rock(rock_c + 3, rock_r, tunnel)
        case 1:
            add_rock(rock_c + 1, rock_r, tunnel)
            add_rock(rock_c, rock_r + 1, tunnel)
            add_rock(rock_c + 1, rock_r + 1, tunnel)
            add_rock(rock_c + 2, rock_r + 1, tunnel)
            add_rock(rock_c + 1, rock_r + 2, tunnel)
        case 2:
            add_rock(rock_c, rock_r, tunnel)
            add_rock(rock_c + 1, rock_r, tunnel)
            add_rock(rock_c + 2, rock_r, tunnel)
            add_rock(rock_c + 2, rock_r + 1, tunnel)
            add_rock(rock_c + 2, rock_r + 2, tunnel)
        case 3:
            add_rock(rock_c, rock_r, tunnel)
            add_rock(rock_c, rock_r + 1, tunnel)
            add_rock(rock_c, rock_r + 2, tunnel)
            add_rock(rock_c, rock_r + 3, tunnel)
        case 4:
            add_rock(rock_c, rock_r, tunnel)
            add_rock(rock_c, rock_r + 1, tunnel)
            add_rock(rock_c + 1, rock_r, tunnel)
            add_rock(rock_c + 1, rock_r + 1, tunnel)


with open("day17/input") as file:
    start = time.time()
    gas_shot = [0]
    gas = file.read().strip()
    tunnel = [[1] * 7]
    for i in range(2022):
        simulate_fall(tunnel, gas, i % 5)
    print(len(tunnel) - 1)
    print(int(time.time() - start))
