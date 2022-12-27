with open("day1/input") as file:
    best_count = 0
    best_count2 = 0
    best_count3 = 0
    count = 0
    for line in file.readlines():
        if line == "\n":
            if count > best_count:
                best_count3 = best_count2
                best_count2 = best_count
                best_count = count
            elif count > best_count2:
                best_count3 = best_count2
                best_count2 = count
            elif count > best_count3:
                best_count3 = count
            count = 0
        else:
            count += int(line)
    print(best_count + best_count2 + best_count3)
