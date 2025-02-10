n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)] 

dp = [[0] * len(row) for row in maps]  
dp[0][0] = maps[0][0] 


for i in range(1, n):
    for j in range(i+1):  
        if j == 0:  
            dp[i][j] = dp[i-1][j] + maps[i][j]
        elif j == i: 
            dp[i][j] = dp[i-1][j-1] + maps[i][j]
        else:  
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + maps[i][j]

print(max(dp[n-1]))
