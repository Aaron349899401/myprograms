def painting(lengths):
    width = lengths[0] + lengths[2]
    height = max(lengths[1], lengths[3])
    return 2 * (width + height)

lengths = [1, 2, 3, 1]
print(painting(lengths))