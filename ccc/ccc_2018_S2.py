def rotate(data, N):
    return [[data[N-1-c][r] for c in range(N)] for r in range(N)]

def is_good(data): # BRUH
    for r in range(N):
        for c in range(N - 1):
            if data[r][c] > data[r][c + 1]:
                return False
    for c in range(N):
        for r in range(N - 1):
            if data[r][c] > data[r + 1][c]:
                return False
    return True

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]


for _ in range(4):
    if is_good(data):
        break
    data = rotate(data, N)

for i in data:
    print(i)
