N = int(input("Enter: "))
change = list(map(int, input("Enter").split()))

pos = 1
pref = [0] * (N + 1)

for i in range(1, N):
    pref[i] = pref[i - 1] + change[i - 1]
    if pref[i] < 0:
        pos = i + 1 
        break
    else:
        pos = N

print(pos)