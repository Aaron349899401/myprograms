N = int(input("Enter your number of segments: "))
segments = [tuple(map(int, input("Enter your segment info: ").split())) for _ in range(N)]
segments.sort(key=lambda x: -x[1])

pos = 0
for p, at in segments:
    if p == pos:
        pos += 1