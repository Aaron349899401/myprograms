def sun(weather):
    n = len(weather)
    longest = 0

    for i in range(n):
        flipped = weather[:]
        flipped[i] = "S"

        curr = 0
        best = 0
        for w in flipped:
            if w == "S":
                curr += 1
                best = max(best, curr)
            else:
                curr = 0
        longest = max(longest, best)
    return longest