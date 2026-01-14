def once(numbers):
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    for number, value in freq.items():
        if value == 1:
            return number
    return None

numbers = [4, 6, 5, 2, 6, 5]
print(once(numbers))