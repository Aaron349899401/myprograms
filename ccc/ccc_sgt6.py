def boat(weights, limit):
    i = 0
    j = len(weights) - 1
    total = 0
    while i <= j:
        if weights[i] + weights[j] <= limit: # two pointers
            i += 1
        j -= 1
        total += 1
    return total

weights = list(map(int, input("Enter your weights: ").split()))
limit = int(input("Enter your weight limit: "))
print(boat(weights, limit))