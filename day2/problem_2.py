def compute_score(opponent, me):
    shape_opponent = ord(opponent) - 65
    shape_me = ord(me) - 88
    score = shape_me + 1
    if shape_me == shape_opponent:
        return score + 3
    elif ((shape_opponent + 1) % 3) == shape_me:
        return score + 6
    else:
        return score


def find_shape(opponent, me):
    shape_opponent = ord(opponent) - 65
    desired_outcome = ord(me) - 89
    target_shape = (shape_opponent + desired_outcome) % 3
    letter = chr(target_shape + 88)
    return letter


def play(opponent, me):
    me = find_shape(opponent, me)
    return compute_score(opponent, me)


with open("day2/input") as file:
    score = 0
    for line in file.readlines():
        new_score = play(*line.split())
        print(new_score)
        score += new_score
    print(score)
