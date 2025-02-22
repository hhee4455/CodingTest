def solution(n, computers):
    visited = [False] * n
    count = 0
    
    def dfs(computers,index,visited):
        visited[index] = True
        for i in range(n):
            if computers[index][i] == 1 and not visited[i]:
                dfs(computers,i,visited)
    
    for i in range(n):
        if not visited[i]:
            dfs(computers,i,visited)
            count += 1
            
    return count
            
    
    