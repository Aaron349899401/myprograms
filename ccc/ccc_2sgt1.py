def max_dis(ints):
    ints.sort()
    return ints[-1] - ints[0]

ints = list(map(int, input("Enter your integers: ").split()))
print(max_dis(ints))