def nailedit(N, boards):
    boards.sort()
    lengths = {}
    max_length = 0
    l = 0
    r = N - 1
    while l <= r:
        curr = boards[l] + boards[r]
        lengths[curr] = lengths.get(curr, 0) + 1
        l += 1
        r -= 1

    if len(lengths.keys()) == 1:
        max_length = max(*lengths.values(), 0)
        return max_length, 1

    else:
        max_length = max(lengths.values())
        heigths = 0
        while heights <= max_length


# Copilot
def solve():
    import sys
    input = sys.stdin.readline

    N = int(input())
    woods = list(map(int, input().split()))

    MAXL = 2000  # max wood length
    freq = [0] * (MAXL + 1)

    for w in woods:
        freq[w] += 1

    # boards[s] = number of boards of length s
    boards = [0] * (2 * MAXL + 1)

    # Count pairs for each possible sum
    for i in range(1, MAXL + 1):
        if freq[i] == 0:
            continue
        for j in range(i, MAXL + 1):
            if freq[j] == 0:
                continue

            s = i + j
            if i == j:
                boards[s] += freq[i] // 2
            else:
                boards[s] += min(freq[i], freq[j])

    best = max(boards)
    count = boards.count(best)

    print(best, count)