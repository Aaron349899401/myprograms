def power(changes):
    current_power = 0
    for s, v in changes:
        if s == "+" and current_power + v <= 100:
            current_power += v 
        elif s == "-" and current_power - v >= 0:
            current_power -= v 
    return current_power