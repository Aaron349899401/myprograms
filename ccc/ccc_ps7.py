def even_odd(nums, queries):
    result = []
    pref = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        pref[i] = nums[i - 1] + pref[i - 1]
    
    for s, e in queries:
        diff = pref[e] - pref[s - 1]
        result.append("EVEN" if diff % 2 == 0 else "ODD")
    return result

