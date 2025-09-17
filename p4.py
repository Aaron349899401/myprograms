# Factors of a Number
import math
start = 1
num = int(input(" give me a number:"))

new_stop = int(math.sqrt(num)) + 1

while start < new_stop:
    if end % start == 0:
        dividend = num // start
        if start != dividend:
            factor_count += 2
        else:
            factor_cout += 1
    start += 1
print(f"{num} has {factor_count} factors.")