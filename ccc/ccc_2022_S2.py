def contraints(must, cant, groups):
    count = 0
    group_of = {}
    for i, group in enumerate(groups):
        for student in group:
            group_of[student] = i # assigning a group number to a student using indexes
    for a, b in must:
        if group_of[a] != group_of[b]:
            count += 1
    for a, b in cant:
        if group_of[a] == group_of[b]:
            count += 1
    return count

X = 3
must = [tuple(input("Enter your musts: ").split()) for _ in range(X)]
Y = 2
cant = [tuple(input("Enter your cantss: ").split()) for _ in range(Y)]
G = 4
groups = [tuple(input("Enter your groups: ").split()) for _ in range(G)]

print(contraints(must, cant, groups))