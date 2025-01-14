from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(start):
    queue = deque([start])
    visited[start] = 0  
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if visited[node] == -1:
                queue.append(node)
                visited[node] = visited[v] + 1 

bfs(x)

found = False
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        found = True
        
if not found:
    print(-1)
