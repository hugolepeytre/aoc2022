def find_smallest(graph, threshold):
    count = 0
    smallest_size = 70000000
    for el in graph:
        if isinstance(el, int):
            count += el
        else:
            subcount, subsmallest_size = find_smallest(el, threshold)
            count += subcount
            if subsmallest_size < smallest_size:
                smallest_size = subsmallest_size
    if smallest_size > count and count > threshold:
        smallest_size = count
    return count, smallest_size


def count_graph(graph):
    count = 0
    total_count = 0
    for el in graph:
        if isinstance(el, int):
            count += el
        else:
            subcount, subtotal_count = count_graph(el)
            count += subcount
            total_count += subtotal_count
    if count < 100000:
        total_count += count
    return count, total_count


def make_graph(ls):
    graph = []
    current_input = ls[0]
    ls = ls[1:]
    for instr in current_input.split("\n"):
        word1, *_ = instr.split()
        if word1 == "$":
            return graph, ls
        if word1 == "dir":
            subgraph, new_ls = make_graph(ls)
            ls = new_ls
            graph.append(subgraph)
        else:
            graph.append(int(word1))
    return graph, ls


with open("day7/input") as file:
    graph, _ = make_graph(file.read().split("$ ls\n")[1:])
    count, total_count = count_graph(graph)
    print(count)
    available_memory = 70000000 - count
    needed_size = 30000000 - available_memory
    print(needed_size)
    count, smallest_size = find_smallest(graph, needed_size)
    print(smallest_size, count)
