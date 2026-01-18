def cookies(greed, cookie_size):
    greed.sort()
    cookie_size.sort()
    i = 0
    j = 0
    count = 0
    while i < len(greed) and j < len(cookie_size):
        if greed[i] <= cookie_size[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

greed = list(map(int, input("Enter your list of greed factors: ").split()))
cookie_size = list(map(int, input("Enter your list of cookie sizes: ").split()))
print(cookies(greed, cookie_size))