from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# 거리 저장용 배열 (-1로 초기화하면서, 벽(0)은 그대로 유지)
distance = [[-1 if maps[i][j] != 0 else 0 for j in range(m)] for i in range(n)]

# 시작 위치 찾기
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            start_x, start_y = i, j
            maps[i][j] = 0  # 원본 지도에서 2를 0으로 변경 (출발점)
            distance[i][j] = 0  # 시작 위치 거리 = 0

# 방향 이동 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([(start_x, start_y)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위를 벗어나면 무시
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
            
        # 이동할 수 없는 곳(벽)인 경우 무시
        if maps[nx][ny] == 0:
            continue
        
        # 아직 방문하지 않은 곳이라면 거리 갱신
        if distance[nx][ny] == -1:  # 방문하지 않은 경우
            distance[nx][ny] = distance[x][y] + 1
            queue.append((nx, ny))

# 결과 출력
for row in distance:
    print(*row)
