def score(scores):
    results = []
    for score, k in scores:
        max_num = score[1]
        new = score
        for i in range(k):
            if score[i] > max_num:
                new = new - score[i]