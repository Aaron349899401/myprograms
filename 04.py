# Painting Fences
from math import ceil
Fence1 = len(str(input("input 'F' for each fence plank: ")))
Fence2 = len(str(input("input 'F' for each fence plank: ")))
Fence3 = len(str(input("input 'F' for each fence plank: ")))

Total = Fence1 + Fence2 + Fence3
rni = ceil(Total / 12)
print(rni)
print(Total % 12)
print(Total * 14.95)