def robo_revisit(directions):
    if not directions:
        return True
    visited = set()
    x = 0
    y = 0
    visited.add((x, y))
    for direction in directions:
        if direction == "N":
            y += 1
        elif direction == "S":
            y -= 1
        elif direction == "E":
            x += 1
        elif direction == "W":
            x -= 1
        if (x, y) in visited:
            return True
        visited.add((x, y))
    return False

directions = input("Enter your directions: ")

result = robo_revisit(directions)
if result:
    print("YES")
else:
    print("NO")