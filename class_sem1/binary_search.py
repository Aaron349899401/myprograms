def bin_search(a_list, target):
    low = 0
    high = len(a_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] == target:
            return mid
        elif a_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

peepee = input("Enter your list: ")
a_list = [x.strip() for x in peepee.split(",")]
a_list.sort()
target = input("Enter your target value: ")
result = bin_search(a_list, target)
print(f"target value: {target}, index: {result}")

def bin(li, targ):
    low = 0
    high = len(li) - 1
    while low <= high:
        mid = (high - low)/2
        if mid == targ:
            return True
        elif targ > mid:
            low = mid
        elif targ < mid:
            high = mid