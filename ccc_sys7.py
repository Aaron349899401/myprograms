import sys, re

averages = []
for line in sys.stdin:
    nums = re.findall(r"-?\d+", line)
    if not nums:
        continue
    nums = list(map(int, nums))
    averages.append(sum(nums) / len(nums))

for ave in averages:
    sys.stdout.write(str(ave) + "\n")

