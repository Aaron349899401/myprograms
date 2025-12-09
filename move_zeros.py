# method 1
def boobies(nums):
    for num in nums:
        if num == 0:
            nums.remove(num)
            nums.append(num)
    return nums

# sometimes we want a list filled w/ placeholder
# sometimes we can have two pointers
# Remembers complexity
# only works with wat you have been given, therefore it is faster (method 2)

# method 2
def boobs(nums):
    poop = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[poop], nums[i] = nums[i], nums[poop] 
            poop += 1
    return nums

def moveZeroes2(nums):
    temp = [0] * len(nums)
    i = 0
    for num in nums:
        if num != 0:
            temp[i] = num
            i += 1
    nums = temp
    return nums

nums = [0,1,0,3,12]
print(boobs(nums))