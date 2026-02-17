from sympy import isprime
def average_primes(numbers):
    results = []
    for n in numbers:
        lim = n * 2
        for p in range(2, lim):
            if isprime(p) and isprime(lim - p):
                result.append((p, lim - p))
                break
    return results

# Copilot Solution
def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

for _ in range(T):
    n = int(input())
    target = n * 2
    p = 2
    while True:
        if is_prime(p) and is_prime(target - p):
            print(p, target - p)
            break
        p += 1        

