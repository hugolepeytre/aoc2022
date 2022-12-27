def compare(elem1, elem2):
    # 0 if smaller, 1 if bigger, 2 if eq
    if isinstance(elem1, int):
        if isinstance(elem2, int):
            return (elem1 >= elem2) + (elem1 == elem2)
        else:
            return compare([elem1], elem2)
    else:
        if isinstance(elem2, int):
            return compare(elem1, [elem2])
        else:
            for i in range(min(len(elem1), len(elem2))):
                result_compare = compare(elem1[i], elem2[i])
                if result_compare < 2:
                    return result_compare
            return compare(len(elem1), len(elem2))


with open("day13/input") as file:
    count = 0
    for i, pair in enumerate(file.read().split("\n\n")):
        line1, line2 = pair.split("\n")
        list1 = eval(line1)
        list2 = eval(line2)
        try:
            if compare(list1, list2) == 0:
                count += i + 1
            pass
        except RecursionError:
            pass
    print(count)
