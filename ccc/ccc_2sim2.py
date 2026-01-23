M = int(input("Enter your number of actions: "))

current = 100
for _ in range(M):
    act = input("Enter your action: ").split()
    if act[0] == "U":
        steps = int(act[1])
        new_current = current - steps
        if new_current < 0: # new_current is not needed 
            new_current = 0
        current = new_current
    elif act[0] == "C":
        steps = int(act[1])
        new_current = current + steps
        if new_current > 100:
            new_current = 100
        current = new_current

print(current)
