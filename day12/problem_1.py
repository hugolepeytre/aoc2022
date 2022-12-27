with open("day12/input") as file:
    grid = []
    start = None
    end = None
    for line in file.readlines():
        int_line = list([ord(x) for x in line.strip()])
        if 83 in int_line:
            idx_start = int_line.index(83)
            start = (idx_start, len(grid))
            int_line[idx_start] = 97
        if 69 in int_line:
            idx_end = int_line.index(69)
            end = (idx_end, len(grid))
            int_line[idx_end] = 122
        grid.append(int_line)
    visited = set()
    marked = [(start, 0)]
    while len(marked) > 0:
        (current_x, current_y), distance = marked.pop(0)
        if (current_x, current_y) == end:
            print(distance)
            exit()
        if not (current_x, current_y) in visited:
            if (
                current_x > 0
                and grid[current_y][current_x - 1] <= grid[current_y][current_x] + 1
            ):
                marked.append(((current_x - 1, current_y), distance + 1))
            if (
                current_y > 0
                and grid[current_y - 1][current_x] <= grid[current_y][current_x] + 1
            ):
                marked.append(((current_x, current_y - 1), distance + 1))
            if (
                current_x < len(grid[0]) - 1
                and grid[current_y][current_x + 1] <= grid[current_y][current_x] + 1
            ):
                marked.append(((current_x + 1, current_y), distance + 1))
            if (
                current_y < len(grid) - 1
                and grid[current_y + 1][current_x] <= grid[current_y][current_x] + 1
            ):
                marked.append(((current_x, current_y + 1), distance + 1))
        visited.add((current_x, current_y))
