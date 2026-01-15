def quad(x, y):
    if x > 0 and y > 0:
        return "Quadrant 1"
    elif x > 0 and y < 0:
        return "Quadrant 4"
    elif x < 0 and y > 0:
        return "Quadrant 3"
    elif x < 0 and y < 0:
        return "Quadrant 3"
        
x = int(input("Enter your x-coordinate: "))
y = int(input("Enter your y-coordinate: "))
print(quad(x, y))