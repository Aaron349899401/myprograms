def pigga(total, chores):
    count = 0
    bruh = 0
    poopy = sorted(chores) #.sort() is based on merge short
    for x in poopy:
        if bruh + x <= total:
            bruh += x
            count += 1
        else:
            break
    return count

chore_count = 0
# Mr.Park solution
while total > 0 and chores:
    total -= chores[0] # continously subtracts the smallles value
    chore_count += 1 # what we're gonna return
    chores.pop(0) # why not .remove?, this line ensures it does not subtract the same smallest value again
# .pop() is not ideal because it shifts all of the list items each time, making a O(1) into O(n)
total = int(input("Enter: "))
num_of_chores = int(input("Enter: "))
chores = [int(input("Enter your chore time: ")) for _ in range(1, num_or_chores+1)]

print(pigga(total, chores))