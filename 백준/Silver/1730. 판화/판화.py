# 입력 받기
N = int(input())
commands = input()

# 목판 초기화
board = [['.' for _ in range(N)] for _ in range(N)]

# 초기 위치
x, y = 0, 0

# 이동 명령 처리
for command in commands:
    # 현재 위치 표시
    if command == 'U':
        if x > 0:  # 격자 밖으로 나가지 않게 조건 확인
            if board[x][y] == '.':
                board[x][y] = '|'
            elif board[x][y] == '-':
                board[x][y] = '+'
            x -= 1
            if board[x][y] == '.':
                board[x][y] = '|'
            elif board[x][y] == '-':
                board[x][y] = '+'
    elif command == 'D':
        if x < N - 1:  # 격자 밖으로 나가지 않게 조건 확인
            if board[x][y] == '.':
                board[x][y] = '|'
            elif board[x][y] == '-':
                board[x][y] = '+'
            x += 1
            if board[x][y] == '.':
                board[x][y] = '|'
            elif board[x][y] == '-':
                board[x][y] = '+'
    elif command == 'L':
        if y > 0:  # 격자 밖으로 나가지 않게 조건 확인
            if board[x][y] == '.':
                board[x][y] = '-'
            elif board[x][y] == '|':
                board[x][y] = '+'
            y -= 1
            if board[x][y] == '.':
                board[x][y] = '-'
            elif board[x][y] == '|':
                board[x][y] = '+'
    elif command == 'R':
        if y < N - 1:  # 격자 밖으로 나가지 않게 조건 확인
            if board[x][y] == '.':
                board[x][y] = '-'
            elif board[x][y] == '|':
                board[x][y] = '+'
            y += 1
            if board[x][y] == '.':
                board[x][y] = '-'
            elif board[x][y] == '|':
                board[x][y] = '+'

# 출력
for row in board:
    print(''.join(row))
