from collections import deque

n = int(input())
maps = [list(map(int,input().split())) for _ in range(n)]
area = []

max_height = max(map(max, maps))

directions = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x,y,visited,height):
    queue = deque([(x,y)])
    visited[x][y] = True

    while queue:
        cx,cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and maps[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))
                
max_safe_areas = 1
for height in range(1,max_height+1):
    visited = [[False] * n for _ in range(n)]
    safe_areas = 0

    for i in range(n):
        for j in range(n):
            if maps[i][j] > height and not visited[i][j]:
                bfs(i,j,visited,height)
                safe_areas += 1
    max_safe_areas = max(max_safe_areas, safe_areas)

print(max_safe_areas)
    
    