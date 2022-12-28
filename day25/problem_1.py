import time


def int_to_base5(x):
    if x == 0:
        return 0

    base_digits = [i for i in range(5)]
    digits = []

    while x:
        digits.append(str(base_digits[x % 5]))
        x = x // 5

    digits.reverse()
    return "".join(digits)


def snafu_to_base10int(s):
    res = 0
    pow = 1
    for snafu_digit in s[::-1]:
        match snafu_digit:
            case "=":
                res -= 2 * pow
            case "-":
                res -= pow
            case _:
                res += int(snafu_digit) * pow
        pow *= 5
    return res


def base5str_to_snafu(s):
    digits = []
    overflow = 0
    for d in s[::-1]:
        d = int(d)
        d += overflow
        overflow = d // 5
        d = d % 5
        if d > 2:
            d -= 5
            overflow += 1
        digits.append(int_to_snafu_digit(d))
    return "".join(digits)[::-1]


def int_to_snafu_digit(d):
    if d > 2 or d < -2:
        raise BaseException
    if d >= 0:
        return str(d)
    if d == -1:
        return "-"
    if d == -2:
        return "="


with open("inputs/day25/input") as file:
    start = time.time()
    sum = 0
    for line in file.readlines():
        sum += snafu_to_base10int(line.strip())
    print(f"Sum : {sum}")
    print(f"In SNAFU base : {base5str_to_snafu(int_to_base5(sum))}")
    print(f"Ran in {int(time.time() - start)}s")
