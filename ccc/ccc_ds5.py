def highest_score(scores):
    my_dih = {}
    for person in scores:
        name, score = person.split()
        my_dih[name] = int(score)
    max_score = max(my_dih.values())
    return "".join([x for x, y in my_dih.items() if y == max_score])

N = int(input("Enter your number of people: "))
scores = []
for _ in range(N):
    scores.append(input("Enter your score: "))
print(highest_score(scores))