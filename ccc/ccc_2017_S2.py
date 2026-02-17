N = 8  # CORRECT!
raw = [10, 50, 40, 7, 3, 110, 90, 2]
raw.sort()
l = N // 2 - 1
r = N // 2 
measurements = []
while l >= 0 and r < N:
    measurements.append(raw[l])
    measurements.append(raw[r])
    l -= 1
    r += 1

print(*measurements)