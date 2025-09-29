def perf(num):
    divider = 1
    total = 0
    while divider < num:
        if num % divider == 0:
            total += divider
        divider += 1
    return total == num

number = 1
while number <= 1000000:
    if perf(number):
        print(f"{number} is a perfect number!")
    number += 1