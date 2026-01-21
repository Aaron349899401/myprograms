def street(lights, queries):
    # Build prefix sum array
    pref = [0] * (len(lights) + 1)
    for i in range(1, len(lights) + 1):
        pref[i] = pref[i - 1] + lights[i - 1]

    # Answer queries in O(1)
    result = []
    for L, R in queries:
        result.append(pref[R] - pref[L - 1])
    return result


lights = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1]
Q = 3
queries = [tuple(map(int, input("Enter your request: ").split())) for _ in range(Q)]

on = street(lights, queries)
for i in on:
    print(i)