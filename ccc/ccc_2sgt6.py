def refueling(refuels, fuel, distance):
    refuels.sort(key=lambda x: x[0])
    current_fuel = fuel
    refuel_count = 0
    for i in range(len(refuels)):
        if current_fuel >= distance:
            break
        elif refuels[i][0] <= current_fuel and current_fuel < refuels[i+1][0]:
            current_fuel += refuels[i][1]
            refuel_count += 1
        else:
            if current_fuel >= refuels[i+1][0]:

        

N = 4
refuels = [(10, 10), (20, 20), (30, 30), (60, 40)]
fuel = 10
distance = 100