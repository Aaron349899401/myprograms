def rainfall(amounts, queries):
    result = []
    for q in queries:
        s, e = map(lambda x: x-1, q)
        result.append(sum(amounts[s:e+1])) # exact same as ps1?
    return result

amounts = [2, 0, 5, 1, 3, 4, 6]
Q = 2
queries = [tuple(map(int, input("Enter your question: ").split())) for _ in range(Q)]

print(rainfall(amounts, queries))