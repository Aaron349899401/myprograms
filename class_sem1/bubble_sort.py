def bubble(sort):
    sumting = True
    while sumting:
        sumting = False
        for i in range(1, len(sort)):
            if sort[i] < sort[i-1]:
                sort[i-1], sort[i] = sort[i], sort[i-1]
                sumting = True
    result = []
    previous = None
    count = 0
    for item in sort:
        if item == previous:
            count += 1
            result.append(f"{item}({count})")
        else:
            count = 0
            result.append(item)
        previous = item
    return result

wow = input("Enter your string: ")
sort = [x.strip() for x in wow.split(",")]
print(bubble(sort))



def selection(arr):
    n = len(arr)
    for i in range(1, n):
        max = i 
        for j in range(i, n):
            if j > max:
                max = j 
            arr[max], arr[j] = 