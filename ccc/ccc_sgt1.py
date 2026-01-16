def sort(thing):
    swapped = True
    count = 0
    while swapped:
        swapped = False
        for i in range(1, len(thing)):
            if thing[i] < thing[i - 1]:
                thing[i - 1], thing[i] = thing[i], thing[i - 1]
                count += 1
                swapped = True
    return count

def minimum_swaps(arr):
    n = len(arr)
    sorted_arr = sorted(arr)

    # Map value → correct index
    correct_pos = {value: i for i, value in enumerate(sorted_arr)}

    visited = [False] * n
    swaps = 0

    for i in range(n):
        if visited[i] or correct_pos[arr[i]] == i:
            continue

        cycle_size = 0
        j = i

        while not visited[j]:
            visited[j] = True
            j = correct_pos[arr[j]]
            cycle_size += 1

        swaps += cycle_size - 1

    return swaps

thing = [4, 3, 2, 1, 5]
print(sort(thing))