def bouncing(start, direction, time, largest):
    final_pos = 0
    if direction == "R":
        final_pos = largest - (time - largest - start)
    elif direction == "L":
        final_pos = time - start
    return final_pos

# Copilot solution: 
def bouncing(start, direction, time, largest):
    # Convert direction to +1 or -1
    dir = 1 if direction == "R" else -1

    # Move on the unfolded line
    pos = start + dir * time

    # Modulo the cycle length
    cycle = 2 * largest
    pos %= cycle # modulus tells you here you are in a repeating cycle

    # Fold back into [0, N]
    if pos > largest:
        pos = cycle - pos

    return pos