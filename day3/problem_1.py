def get_outlier(sack):
    comp1, comp2 = sack[: len(sack) // 2], sack[len(sack) // 2 :]
    for char in comp1:
        if char in comp2:
            return char


def compute_score(sack):
    outlier = ord(get_outlier(sack))
    if outlier <= 90:
        return outlier - 65 + 27
    else:
        return outlier - 96


with open("day3/input") as file:
    score = 0
    for line in file.readlines():
        new_score = compute_score(*line.split())
        score += new_score
    print(score)
