def bubble(sort):
    sumting = True
    while sumting:
        sumting = False
        for i in range(1, len(sort)):
            if sort[i] < sort[i-1]:
                sort[i-1], sort[i] = sort[i], sort[i-1]
                sumting = True
    for index, item in enumerate(sort):
        count = 0
        if sort[index] == sort[index-1]:
            count += 1
        sort[index] += f"({count})"
    return sort

wow = input("Enter your string: ")
sort = [x.strip() for x in wow.split(",")]
print(bubble(sort))

