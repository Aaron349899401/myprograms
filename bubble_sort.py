def bubble(sort):
    i = 0
    for n in range(len(sort)**2):
        other = sort[i]
        if sort[i] < sort[i+1]:
            sort.replace(sort[i], sort[i+1])
            sort.replace(sort[i+1], other)
        new_sort = sort
    return new_sort

sort = input("Enter your string: ")
print(bubble(sort))