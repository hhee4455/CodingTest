from collections import deque

def solution(board):
    # 보드 크기
    n, m = len(board), len(board[0])
    
    # 로봇의 시작 위치(R)와 목표 위치(G) 찾기
    start = goal = None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
    
    # 방향 이동 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # BFS 초기화
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, steps = queue.popleft()
        
        # 목표 지점 도달 시 이동 횟수 반환
        if (x, y) == goal:
            return steps
        
        # 4방향으로 이동
        for dx, dy in directions:
            nx, ny = x, y
            
            # 해당 방향으로 끝까지 미끄러짐
            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy
            
            # 이동한 위치가 방문하지 않은 곳이면 큐에 추가
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    
    # BFS 끝나도 목표에 도달하지 못하면 -1 반환
    return -1