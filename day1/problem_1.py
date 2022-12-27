with open("day/input") as file:
    best_count = 0
    count = 0
    for line in file.readlines():
        if line == "\n":
            if count > best_count:
                best_count = count
            count = 0
        else:
            count += int(line)
    print(best_count)
