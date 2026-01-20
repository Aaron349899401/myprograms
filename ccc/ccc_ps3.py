def average(marks, queries):
    result = []
    for q in queries:
        f, l = map(lambda x: x-1, q)
        result.append(sum(marks[f:l+1]) // (l + 1 - f))
    return result

marks = [70, 80, 90, 60, 100, 75]
Q = 2
queries = [tuple(map(int, input("Enter your query: ").split())) for _ in range(Q)]

print(average(marks, queries))