N = int(input("Enter: "))
# WRONG
curr = 1
for i in range(2, N):
    if curr + i == N:
        result = True
        curr = i 

if result:
    print("YES")
else:
    print("NO")