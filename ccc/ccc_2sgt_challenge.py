def group_sum(arr, k):
    arr.sort()
    mid = len(arr) // k
    for num in arr:

# Copilot Solution:
def can_split(nums, K, limit):
    groups = 1
    current = 0

    for x in nums:
        if x > limit:
            return False  # impossible if a single number exceeds limit

        if current + x <= limit:
            current += x
        else:
            groups += 1
            current = x
            if groups > K:
                return False

    return True


def minimize_largest_group(nums, K):
    left = max(nums)          # smallest possible max group sum
    right = sum(nums)         # largest possible max group sum

    while left < right:
        mid = (left + right) // 2

        if can_split(nums, K, mid):
            right = mid
        else:
            left = mid + 1

    return left


# Input handling
N = int(input())
nums = list(map(int, input().split()))
K = int(input())

print(minimize_largest_group(nums, K))