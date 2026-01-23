N = int(input("Enter your number of towers: "))
T = int(input("Enter your time: "))

towers = list(map(int, input("Enter your locations: ").split()))

# Determine coverage range
left_bound = min(towers) - T
right_bound = max(towers) + T

# Create coverage array
size = right_bound - left_bound + 1
line = [False] * size

for t in towers:
    l = t - T
    r = t + T
    for pos in range(l, r + 1):
        line[pos - left_bound] = True

print(sum(line))