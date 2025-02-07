from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(0, 0, 1)]) 

while queue:
    x, y, distance = queue.popleft()
    
    if x == n - 1 and y == m - 1:
        print(distance)
        break 

    maps[x][y] = 0  

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue

        if maps[nx][ny] == 1:
            queue.append((nx, ny, distance + 1))
            maps[nx][ny] = 0  
