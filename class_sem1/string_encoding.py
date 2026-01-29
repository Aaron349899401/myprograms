def boobs(poopy):
    new_poopy = []
    if not poopy:
        return new_poopy
    current = poopy[0]
    count = 1
    for i in range(1, len(poopy)):
        if poopy[i] == current:
            count += 1
        else:
            new_poopy.append(current)
            new_poopy.append(count)
            current = poopy[i]
    new_poopy.append(current)

def decoder(poopy):
    if not poopy:
        return -1
    
 
poopy = ["AAABBBCCDEE"]
print(boobs(poopy))
        