n = int(input()) 
m = int(input())  

graph = [[] for _ in range(n + 1)]  
visited = [False] * (n + 1) 


for _ in range(m):
    com, next_com = map(int, input().split())
    graph[com].append(next_com)
    graph[next_com].append(com)  

def dfs(start):
    visited[start] = True  
    for network in graph[start]:  
        if not visited[network]: 
            dfs(network)

dfs(1)

print(sum(visited) - 1)
