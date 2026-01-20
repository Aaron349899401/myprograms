def builder(lih1, lih2):
    tape = 0
    for i in range(1, len(lih1)):
        if lih1[i] == 1:
            tape += 3
            if lih1[i+1] == 1:
                tape += 2
            elif lih1[i-1] == 1:
                tape += 2
        elif lih1[i] == 1 and lih2[i] == 1:
            tape += 5
        elif lih2[i] == 1:

    return tape

N = int(input("Enter your number of columns: "))
lih1 = list(map(int, input("Enter your first row: ").split()))
lih2 = list(map(int, input("Enter your second row: ").split()))

print(builder(lih1, lih2))