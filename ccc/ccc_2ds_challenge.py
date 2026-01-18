def compress(arr):
    done = sorted(set(arr))
    rank = {}
    for i, value in enumerate(done):
        rank[value] = i 
    ski = []
    for bruh in arr:
        ski.append(rank[bruh])
    return " ".join(map(str, ski))

# other method (from chat)
def compress(arr):
    rank = {v: i for i, v in enumerate(sorted(set(arr)))} # uses index as the ranking system
    return " ".join(str(rank[x]) for x in arr)

arr = [100, 500, 300, 500, 100]
print(compress(arr))