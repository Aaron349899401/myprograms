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