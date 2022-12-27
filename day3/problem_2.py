def get_outlier(sack1, sack2, sack3):
    for char in sack1:
        if char in sack2 and char in sack3:
            return char


def compute_score(sacks):
    outlier = ord(get_outlier(*sacks))
    if outlier <= 90:
        return outlier - 65 + 27
    else:
        return outlier - 96


with open("day3/input") as file:
    score = 0
    lines = file.readlines()
    for i in range(0, len(lines), 3):
        score += compute_score(lines[i : i + 3])
    print(score)
