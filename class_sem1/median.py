def median(data):
    high = len(data)
    mid = high // 2
    if high % 2 == 0:
        return (data[mid - 1] + data[mid])/2
    else:
        return data[mid]

def mean(data):
    return sum(data) / len(data)

data = [1, 2, 3, 4, 5, 6, 7]
print(median(data))
print(mean(data))