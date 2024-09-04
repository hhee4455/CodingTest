n = int(input())
result = [0,1]

for i in range(1,45):
    result.append(result[i-1]+result[i])

print(result[n])