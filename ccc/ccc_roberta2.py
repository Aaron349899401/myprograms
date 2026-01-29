from collections import deque
def golf(target, clubs):
    q = deque([(0, 0)])
    visited = {0}
    while q:
        pos, swings = q.popleft()

        for c in clubs:
            new_pos = pos + c

            if new_pos == target:
                return swings + 1

            if new_pos < target and new_pos not in visited:
                q.append((new_pos, swings + 1))
                visited.add(new_pos)
    return False

target = int(input("Enter: "))
N = int(input("Enter your number of clubs: "))
clubs = list(map(int, input("Enter your club: ")) for _ in range(N))

result = golf(target, clubs)
if result:
    print(f"Roberta wins in {result} strokes!")
else: 
    print("Roberta accepts defeat.")