def count_friend_groups(n, friendships):
    # Build adjacency list
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)

    visited = set()
    groups = 0

    def dfs(node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    # Count connected components
    for student in range(1, n + 1):
        if student not in visited:
            groups += 1
            dfs(student)

    return groups


# Example of how input might be handled:
# (You can adjust this depending on your exact input format)

n = int(input())  # number of students
m = int(input())  # number of friendships

friendships = []
for _ in range(m):
    a, b = map(int, input().split())
    friendships.append((a, b))

print(count_friend_groups(n, friendships))