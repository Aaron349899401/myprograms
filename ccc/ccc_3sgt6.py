def boats(weights, limit):
    weights.sort()
    count = 0
    l = 0
    r = len(weights) - 1
    while l <= r: # you have to use <= because otherwise you wouldn't include one person
        if weights[l] + weights[r] <= limit:
            l += 1
        r -= 1
        count += 1
    return count

weights = list(map(int, input("Enter your list of weights: ").split()))
limit = int(input("Enter your weight limit: "))
print(boats(weights, limit))