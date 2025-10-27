def sort_wow(list1, list2):
    noway = True
    while noway:
        noway = False
        for i in range(1, len(list1)):
            if list1[i-1] > list1[i]:
                list1[i-1], list1[i] = list1[i], list1[i-1]
                list2[i-1], list2[i] = list2[i], list2[i-1]
    return list1, list2

list1_input = input("Enter your first list: ")
list1 = [x.strip() for x in list1_input.split(",")]
list2_input = input("Enter your second list: ")
list2 = [x.strip() for x in list2_input.split(",")]
print(sort_wow(list1, list2))