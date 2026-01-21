def fence(heights, widths):
    area = 0
    for w in range(len(widths)):
        h1, h2 = heights[w], heights[w+1]
        area += widths[w]*(h1 + h2) / 2
    return area

N = int(input("Enter your number: "))
heights = list(map(int, input("Enter your heights: ").split()))
widths = list(map(int, input("Enter your widths: ").split()))

print(fence(heights, widths))