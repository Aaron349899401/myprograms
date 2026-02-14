def donuts(starting, events):
    result = starting
    for sign, quant in events:
        if sign == "+":
            result += quant
        else:
            result -= quant
    return result

starting = int(input("Enter: "))
E = int(input("Enter: "))
events = []
for _ in range(E):
    s, q = input("Enter: ").strip().split()
    events.append((s, int(q)))

print(donuts(starting, events))