def miss(nums):
    max_num = max(nums)
    freq_table = {}
    for x in nums:
        freq_table[x] = 1
    for i in range(0, max_num):
        if i not in freq_table:
            return i
    return "Nothing Missing!"

nums = [0, 1, 2, 3, 5, 6, 7, 8, 9]
print(miss(nums))