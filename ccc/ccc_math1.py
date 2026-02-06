N = int(input("Enter: "))
status = False
for i in range(1, N + 1):
    divisor = N - i 
    if i % 2 == 0 and divisor % 2 == 0:
        status = True

if status:
    print("YES")
else:
    print("NO")