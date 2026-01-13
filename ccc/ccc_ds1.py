def freq(nums):
    my_dih = {}
    for num in nums:
        my_dih[num] = my_dih.get(num, 0) + 1

    max_freq = max(my_dih.values())

    stuff = [num for num, freq in my_dih.items() if freq == max_freq]
    return min(stuff)

nums = list(map(int, input("Enter your numbers: ").split()))
print(freq(nums))

# .split() default is any whitespace