import sys, re

N = int(sys.stdin.readline())

integers = sys.stdin.readline()
nums = re.findall(r"\d+", integers)
even_count = 0

if len(nums) != N:
    sys.stdout.write("Error: incorrect amount of integers in second line.")
else: 
    for num in nums:
        if int(num) % 2 == 0:
            even_count += 1

sys.stdout.write(str(even_count))