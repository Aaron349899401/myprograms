def compress(arr):
    done = sorted(set(arr))
    rank = {}
    for i, value in enumerate(done):
        rank[value] = i 
    ski = []
    for bruh in arr:
        ski.append(rank[bruh])
    return " ".join(map(str, ski))

arr = [100, 500, 300, 500, 100]
print(compress(arr))