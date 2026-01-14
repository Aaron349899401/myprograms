def appears(N, int_list):
    freq = {}
    for num in int_list:
        freq[num] = freq.get(num, 0) + 1
    var = N // 2
    for nummy, value in freq.items():
        if value >= var:
            return nummy
    return "NO"

N = int(input("Enter your quantity of integers: "))
integers = input("Enter your list of integers: ")
int_list = list(map(int, integers.split()))

print(appears(N, int_list))
