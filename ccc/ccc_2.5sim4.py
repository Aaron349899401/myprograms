N = int(input("Enter: "))
pos = int(input("Enter: "))

directions = {
    "R": 1,
    "L": -1,
    "S": False
}

tiles = []
for _ in range(N):
    tile = input("Enter: ")
    tiles.append(tile)

direction = tiles[pos - 1]
visited = set()
visited.add(pos)

while True:
    dm = directions[direction]
    if not dm:
        break
    new_pos = pos + dm

    if not (1 <= new_pos <= N) or new_pos in visited:
        break
    pos = new_pos
    direction = tiles[pos - 1]
    visited.add(pos)

print(pos)