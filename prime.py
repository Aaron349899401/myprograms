# prime
import math
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1, 1000000):
    if prime(num):
        print(num)