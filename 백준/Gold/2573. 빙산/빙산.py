from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for i in range(n)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

def melt_ice():
    new_grid = [[0] * m for _ in range(n)] 

    for x in range(n):
        for y in range(m):
            if grid[x][y] > 0: 
                sea_count = 0 
                for dx, dy in directions: 
                    nx = x + dx  
                    ny = y + dy  
                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] == 0:  
                            sea_count += 1 

                new_grid[x][y] = max(0, grid[x][y] - sea_count)  

    return new_grid

years = 0
while True:
    visited = [[False] * m for _ in range(n)]
    count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited)
                count += 1 

    if count >= 2: 
        print(years)
        break

    if count == 0: 
        print(0)
        break

    grid = melt_ice()
    years += 1  
