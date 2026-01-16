def fin(items, budget):
    items.sort()
    count = 0
    value = 0
    for cost in items:
        if value > budget:
            break
        value += cost
        count += 1
    return count

budget = int(input("Enter your budget: "))
items = list(map(int, input("Enter your item cost: ").split()))

print(fin(items, budget))