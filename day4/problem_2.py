def compute_score(range1, range2):
    begin1, end1 = map(lambda x: int(x), range1.split("-"))
    begin2, end2 = map(lambda x: int(x), range2.split("-"))
    if (begin2 <= begin1 and begin1 <= end2) or (begin1 <= begin2 and begin2 <= end1):
        return 1
    return 0


with open("day4/input") as file:
    score = 0
    for line in file.readlines():
        new_score = compute_score(*line.split(","))
        score += new_score
    print(score)
