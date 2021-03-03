def latest(scores):
    for score in scores:
        if scores.index(score) == len(scores) - 1:
            return score



def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    return sorted(scores, reverse=True)[0:3]
