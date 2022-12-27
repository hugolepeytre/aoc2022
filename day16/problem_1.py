def known_idx(opened, current, step, n_valves):
    return opened + ((current + (step << n_valves)) << n_valves)


def add_to_set(set, new_elem):
    return set | (1 << new_elem)


def check_in_set(set, elem):
    return (set & (1 << elem)) != 0


def reduce_graph(graph, flows, start):
    nonzero_valves = list([valve for valve in range(len(flows)) if flows[valve] > 0])
    nonzero_valves.insert(0, start)
    new_flows = list([flow for flow in flows if flow > 0])
    new_flows.insert(0, 0)

    new_graph = []
    for valve in nonzero_valves:
        all_dists = shortest_paths(graph, valve)
        dists = [all_dists[i] for i in nonzero_valves]
        new_graph.append(dists)
    return new_graph, new_flows


def shortest_paths(graph, valve):
    distances = [len(graph) + 1] * len(graph)
    distances[valve] = 0
    unvisited = set(range(len(graph)))
    while len(unvisited) > 0:
        unvisited_list = sorted(list(unvisited), key=lambda x: distances[x])
        current = unvisited_list[0]
        for next in graph[current]:
            distances[next] = min(distances[next], distances[current] + 1)
        unvisited.remove(current)
    return distances


def parse(file):
    map_names = dict()
    graph = []
    flows = []
    i = 0
    for lines in file.readlines():
        words = lines.split()
        name = words[1]
        flow = int(words[4].split("=")[-1][:-1])
        out = [w.split(",")[0] for w in words[9:]]
        map_names[name] = i
        i += 1
        graph.append(out)
        flows.append(flow)
    graph = [list(map(lambda x: map_names[x], out_valves)) for out_valves in graph]
    start = map_names["AA"]
    graph, flows = reduce_graph(graph, flows, start)
    return graph, flows


def solve(graph, flows, known, current=0, opened=0, step=0):
    if step > 29:
        return 0
    sols = []
    idx = (opened, current, step)
    if idx in known:
        return known[idx]
    if not check_in_set(opened, current):
        value_current_valve = (29 - step) * flows[current]
        sols.append(
            value_current_valve
            + solve(graph, flows, known, current, add_to_set(opened, current), step + 1)
        )
    for next, distance in enumerate(graph[current]):
        if distance > 0:
            sols.append(solve(graph, flows, known, next, opened, step + distance))
    val_sol = max(sols)
    known[idx] = val_sol
    return val_sol


with open("day16/input") as file:
    graph, flows = parse(file)
    known = dict()
    val = solve(graph, flows, known)
    print(val)
