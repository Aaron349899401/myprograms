def skill(students):
    students.sort()
    l = 0
    r = len(students) - 1
    pairs = []
    while l < r:
        if l != r:
            bruh = students[l] + students[r]
            pairs.append(bruh)
        l += 1
        r -= 1
    return max(pairs)

students = [1, 3, 5, 9]
print(skill(students))
