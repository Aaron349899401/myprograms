def mean(data, N):
    return sum([x for x in data]) / N

def bubble(data):
    wow = True
    while wow:
        wow = False
        for i in range(1, len(data)):
            if data[i] < data[i-1]:
                data[i-1], data[i] = data[i], data[i-1]
                wow = True
    return data

def selection_sort(data):
    some = data[:]
    noway = []
    for sumting in some:
        if sumting == min(some):
            noway.append(sumting)
            some.remove(sumting)
    return noway

def median(data):
    sorted_data = bubble(data)
    wow = N // 2
    if len(sorted_data) % 2 == 0:
        return (sorted_data[wow] + sorted_data[wow - 1]) / 2
    else:
        return sorted_data[wow]

data = [2, 3, 3, 6, 5, 9, 10, 100, 14, 17]
N = len(data)
print(mean(data, N))
print(median(data))