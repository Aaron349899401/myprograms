C = int(input())
tiles = [list(map(int, input().split())) for _ in range(2)]
tape = 0
for r in range(2):
    for c in range(C):
        if tiles[r][c] == 0:
            continue

        exposed = 3
        up = (r == 0 and c % 2 == 0) or (r == 1 and c % 2 == 1)

        if c > 0 and tiles[r][c - 1] == 1:
            exposed -= 1
        if c < C - 1 and tiles[r][c + 1] == 1:
            exposed -= 1
        
        if up:
            if r == 0 and tiles[1][c] == 1:
                exposed -= 1
        else:
            if r == 1 and tiles[0][c] == 1:
                exposed -= 1
        tape += exposed

print(tape)