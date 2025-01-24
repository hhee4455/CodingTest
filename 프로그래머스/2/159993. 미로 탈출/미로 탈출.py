from collections import deque

def solution(maps):
    # 시작점, 중간점(L), 끝점(E)의 좌표를 찾기
    for i, row in enumerate(maps):
        if "S" in row:
            s_ind = row.index("S")
            sx, sy = i, s_ind
        if "L" in row:
            l_ind = row.index("L")
            lx, ly = i, l_ind
        if "E" in row:
            e_ind = row.index("E")
            ex, ey = i, e_ind
    
    n = len(maps)  # 행 길이
    m = len(maps[0])  # 열 길이
    dx = [-1, 1, 0, 0]  # 상하좌우 이동
    dy = [0, 0, -1, 1]

    # BFS 함수 정의
    def bfs(sx, sy, tx, ty):
        queue = deque()
        visited = [[False] * m for _ in range(n)]  # 방문 여부 체크
        queue.append((sx, sy, 0))  # (x, y, 거리)
        visited[sx][sy] = True

        while queue:
            x, y, dist = queue.popleft()

            # 목적지에 도달했을 경우 거리 반환
            if x == tx and y == ty:
                return dist

            # 4방향 탐색
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵 범위를 벗어나거나, 벽('X')이거나 이미 방문한 경우 무시
                if nx < 0 or ny < 0 or nx >= n or ny >= m:
                    continue
                if maps[nx][ny] == "X" or visited[nx][ny]:
                    continue

                # 방문하지 않은 경우 큐에 추가 및 방문 표시
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True

        # 목적지에 도달할 수 없는 경우 -1 반환
        return -1

    # 시작점 -> 중간점(L) 거리 계산
    dist_to_l = bfs(sx, sy, lx, ly)
    if dist_to_l == -1:
        return -1  # 중간점에 도달할 수 없는 경우

    # 중간점(L) -> 끝점(E) 거리 계산
    dist_to_e = bfs(lx, ly, ex, ey)
    if dist_to_e == -1:
        return -1  # 끝점에 도달할 수 없는 경우

    # 전체 거리 반환
    return dist_to_l + dist_to_e
