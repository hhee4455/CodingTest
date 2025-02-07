from collections import deque

m, n, h = map(int, input().split()) # m n h

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 토마토는 상하좌우위아래 총 6군데를 익게한다.
# 토마토가 비어져 있는 경우는 익게 하지 못한다.

directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

queue = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                queue.append((z, y, x, 0))  
max_days = 0
while queue:
    z,y,x,days = queue.popleft()
    max_days = max(max_days, days)

    for dz,dy,dx in directions:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = 1 
            queue.append((nz, ny, nx, days + 1))  

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 0:  
                print(-1)
                exit()

print(max_days)
    


        