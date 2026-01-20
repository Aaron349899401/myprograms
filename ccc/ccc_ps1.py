def range_sum(nums, queries):
    result = []
    for q in queries:
        l, u = map(lambda x: x-1, q)
        result.append(sum(nums[l:u+1]))
    return result

nums = [3, 1, 4, 1, 5]
Q = 3
queries = [tuple(map(int, input("Enter your querie: ").split())) for _ in range(Q)]

print(range_sum(nums, queries))