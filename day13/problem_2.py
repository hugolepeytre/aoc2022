from functools import cmp_to_key


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


def custom_compare(item1, item2):
    res = compare(item1, item2)
    if res == 1:
        return 1
    if res == 0:
        return -1
    if res == 2:
        return 0


def bisect_right(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError("lo must be non-negative")
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if compare(x, a[mid]) <= 0:
            hi = mid
        else:
            lo = mid + 1
    return lo


def insort_right(a, x, lo=0, hi=None):
    lo = bisect_right(a, x, lo, hi)
    a.insert(lo, x)


with open("day13/input") as file:
    big_list = []
    for i, pair in enumerate(file.read().split("\n\n")):
        line1, line2 = pair.split("\n")
        list1 = eval(line1)
        list2 = eval(line2)
        big_list.append(list1)
        big_list.append(list2)
    key = cmp_to_key(custom_compare)
    big_list.sort(key=key)
    idx1 = bisect_right(big_list, [[2]]) + 1
    insort_right(big_list, [[2]])
    idx2 = bisect_right(big_list, [[6]]) + 1
    insort_right(big_list, [[6]])
    for e in big_list:
        print(e)
    print(idx1 * idx2)
