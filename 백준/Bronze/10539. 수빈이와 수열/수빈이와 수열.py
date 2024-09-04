n = int(input())
num = list(map(int, input().split()))
result = []
sum = 0

for i in range(1,n+1):
    result.append((i * num[i-1]) - sum)
    sum = result[i-1] + sum

print(*result)