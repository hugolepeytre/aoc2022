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
    print("input", current_input)
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
    print(graph)
    count, total_count = count_graph(graph)
    print(count)
    print(total_count)
