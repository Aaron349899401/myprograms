def infec(n, k, infected, d):
    line = [False] * (n + 1)
    for p in infected:
        l = max(1, p - d) # makes sure l does not go out of bounds (1 to n)
        r = min(n, p + d)
        for i in range(l, r + 1):
            line[i] = True
    return sum(line)