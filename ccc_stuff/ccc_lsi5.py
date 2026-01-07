def location_finder(movement):
    x = 0
    y = 0
    for char in movement:
        if char == "N":
            y += 1
        elif char == "S":
            y -= 1
        elif char == "E":
            x += 1
        elif char == "W":
            x -= 1
    location = x, y
    return location

movement = input("Enter your movements: ")
print(location_finder(movement))