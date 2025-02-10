from collections import deque

x = int(input())
visited = [False] * (x + 1)

queue = deque([(x, 0)])

while queue:
    n, depth = queue.popleft()

    if n == 1:
        print(depth)
        break

    if visited[n]:
        continue

    visited[n] = True  

    if n % 3 == 0:
        queue.append((n // 3, depth + 1))

    if n % 2 == 0:
        queue.append((n // 2, depth + 1))

    queue.append((n - 1, depth + 1))
