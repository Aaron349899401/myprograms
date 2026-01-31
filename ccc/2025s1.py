def wow(bruh):
    pbase = bruh[0] + bruh[2]
    pheight = 0
    if bruh[1] > bruh[3]:
        pheight = bruh[1]
    else:
        pheight = bruh[3]
    return 2*(pbase + pheight)

inh = input("Enter: ")
bruh = [int(x.strip()) for x in inh.split(",")]

print(wow(bruh))