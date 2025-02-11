import sys
sys.setrecursionlimit(10**6) 

t = int(sys.stdin.readline())  
result = []

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m or graph[x][y] == 0:
        return False  

    graph[x][y] = 0 

    dfs(x-1, y)  
    dfs(x+1, y) 
    dfs(x, y-1) 
    dfs(x, y+1) 

    return True

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())  
    graph = [[0] * m for _ in range(n)] 

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1  

    count = 0
    for i in range(n):  
        for j in range(m):  
            if graph[i][j] == 1:  
                if dfs(i, j): 
                    count += 1  

    result.append(str(count))

sys.stdout.write("\n".join(result) + "\n")
