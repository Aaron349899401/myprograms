def closest(numbers):
    numbers.sort()
    smallest_diff = float("inf") 
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] < smallest_diff:
            smallest_diff = numbers[i] - numbers[i-1]
    return smallest_diff

numbers = list(map(int, input("Enter your numbers: ").split()))
print(closest(numbers))