def chores(time, chores):
    chores.sort()
    chore_count = 0
    for c in chores:
        if time - c >= 0:
            time -= c
            chore_count += 1
        else:
            break
    return chore_count