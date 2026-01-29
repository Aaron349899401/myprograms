def merge_sort(amogus):
    # consider me as the splitter
    # BASE CASE
    if len(amogus) <= 1:
        return amogus
    # Work towards the BASE CASE
    mid = len(amogus) // 2
    john = amogus[:mid]
    pork = amogus[mid:]
    
    john = merge_sort(john)
    pork = merge_sort(pork)

    return combine(john, pork)

def combine(john, pork):
    # assume john and pork are sorted
    if len(john) == 0 and len(pork) == 0:
        return []
    elif len(john) == 0:
        return pork
    elif len(pork) == 0:
        return john
    else:
        l = 0
        r = 0
        result = []
        while l < len(john) and r < len(pork):
            if john[l] < pork[r]:
                result.append(john[l])
                l += 1
            else:
                result.append(pork[r])
                r += 1
        while l < len(john):
            result.append(john[l])
            l += 1
        while r < len(pork):
            r += 1

        return result