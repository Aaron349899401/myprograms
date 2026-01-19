def snacks(prices, budget):
    prices.sort()
    count = 0
    for price in prices:
        if budget >= price:
            budget -= price
            count += 1
        else:
            break
    return count

prices = list(map(int, input("Enter your prices: ").split()))
budget = int(input("Enter your budget: "))

print(snacks(prices, budget))