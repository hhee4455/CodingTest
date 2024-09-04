n = int(input())
num = list(map(int,input().split()))

result = max(num) - min(num)

print(result)