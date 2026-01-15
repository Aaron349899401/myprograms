def factorial(num):
    if num == 1: # just do one base case
        return 1
    return num * factorial(num - 1)

num = 4
print(factorial(num))