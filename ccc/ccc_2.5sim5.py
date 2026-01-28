from collections import deque
M = int(input("Enter: "))

platform = None
queue = deque()

for _ in range(M):
    ev, tr = input("Enter your train: ").split()
    
    if ev == "A":
        if platform == None:
            platform = tr
        else:
            queue.append((ev, tr))
    else:
        if platform == tr:
            platform = None
            if queue:
                platform = queue.popleft()
print(platform)