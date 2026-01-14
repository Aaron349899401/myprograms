def prefix(integers):
    seen = set()
    result = []
    for x in integers:
        seen.add(x)
        result.append(len(seen))
    return result

integers = [1, 2, 1, 3, 2]
print(prefix(integers))