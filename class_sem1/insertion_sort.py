def insertion(a_list):
    i = 1 
    while i < len(a_list):
        j = i
        while j > 0:
            if a_list[j-1] > a_list[j]:
                a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            else:
                break
            j -= 1

        i += 1

def insertion_for(a_list):
    for i in range(1, len(a_list)):
        for money in range(i, 0, -1):
            if a_list[money] < a_list[money-1]:
                a_list[money-1], a_list[money] = a_list[money], a_list[money-1]
            else:
                break