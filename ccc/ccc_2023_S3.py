def kita(N, M, R, C):
    if R > N or C > M:
        return "IMPOSSIBLE"
    
    words = [["a" * M] * N]

    for _ in range(R, N + 1):
        for c in range(C, M):
            words[R + 1][c] = "b"
    
    return words

N, M, R, C = map(int, input().split())
result = kita(N, M, R, C)
for i in result:
    print(i)