def groups(nums):
    nums.sort()
    mid = len(nums) // 2
    l = 0
    r = len(nums) - 1
    l_sum = 0
    r_sum = 0
    while l < r:

# solution
# if k isn't hardcoded:
def can_split(nums, K, limit):
    groups = 1
    current = 0

    for x in nums:
        if current + x <= limit:
            current += x
        else:
            groups += 1
            current = x
            if groups > K:
                return False
    return True


def split_array(nums, K):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2
        if can_split(nums, K, mid):
            right = mid
        else:
            left = mid + 1

    return left


N = int(input())
nums = list(map(int, input().split()))
K = int(input())

print(split_array(nums, K))