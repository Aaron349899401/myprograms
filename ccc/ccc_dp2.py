N = int(input("Enter: "))
if N == 1:
    print(2)
    exit() # just a shortcut that allows us to avoid writing an else block
elif N == 2:
    print(3)
    exit()

a, b = 2, 3

for _ in range(3, N + 1):
    a, b = b, a + b 

print(b)