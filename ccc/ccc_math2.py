import math 

a = int(input("Enter your first: "))
b = int(input("Enter your second: "))

low = math.floor(a**0.5)
high = math.ceil(b**0.5)
count = max(0, high - low + 1)

print(count)