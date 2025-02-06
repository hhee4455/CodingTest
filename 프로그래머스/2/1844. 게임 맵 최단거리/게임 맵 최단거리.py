from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0, 1)])

    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]

    while queue:
        x, y, distance = queue.popleft()

        if x == n - 1 and y == m - 1:
            return distance

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True  
                queue.append((nx, ny, distance + 1)) 

    return -1 
