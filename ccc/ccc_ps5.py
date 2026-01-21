def temp_change(temps, queries):
    result = []
    for q in queries:
        s, e = map(lambda x: x-1, q)
        result.append(sum(temps[:e+1]) - sum(temps[:s+1]))
    return result

temps = [10, 12, 15, 14, 13, 16, 18, 17]
Q = 2
queries = [tuple(map(int, input("Enter your query: ").split())) for _ in range(Q)]

diffs = temp_change(temps, queries)
for i in diffs:
    print(i)