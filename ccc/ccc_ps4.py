def at_least(nums, queries):
    result = []
    for q in queries:
        l, r, x = map(lambda x: x-1, q)
        result.append("YES" if sum(nums[l:r+1]) >= x else "NO")
    return result

nums = [5, 1, 3, 2, 4]
Q = 3
queries = [tuple(map(int, input("Enter your query: ").split())) for _ in range(Q)]

result = at_least(nums, queries)
for i in result:
    print(f"Result: {i}")