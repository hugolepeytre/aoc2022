import time


def move(dict, list, e):
    idx = list.index(e)
    new_idx = (idx + dict[e]) % (len(list) - 1)
    list.pop(idx)
    list.insert(new_idx, e)
    return list


with open("day20/input") as file:
    start = time.time()
    indices = [1000, 2000, 3000]
    el_list = [int(x) for x in file.readlines()]
    positions = list(range(len(el_list)))
    for e in range(len(el_list)):
        move(el_list, positions, e)

    positions = [el_list[pos] for pos in positions]
    count = 0
    zero_idx = positions.index(0)
    for i in indices:
        count += positions[(zero_idx + i) % len(positions)]

    print(count)
    print(f"Ran in {int(time.time() - start)}s")
